from langchain_openai import *
from dotenv import load_dotenv
from pathlib import Path
from os import walk
import time
import os
import re

load_dotenv()


def parse_srt(content):
    """
    Parse the content of an SRT file into a dictionary
    """
    if content.startswith("\ufeff1"):
        content=content[1:]
    sections = {}
    parts = re.split(r'\n{2,}', content.strip())
    for part in parts:
        lines = part.splitlines()
        if len(lines) >= 3:
            index = int(lines[0])
            sections[index] = {
                "time": lines[1],
                "text": " ".join(lines[2:]).strip()
            }
    return sections


def check_translate(original, translated):
    """
    Check if the translation contains all sections of the original
    """
    original_sections = parse_srt(original)
    org_length = len(original_sections)
    translated_sections = parse_srt(translated)
    tr_length = len(translated_sections)

    # check for extra part in translation
    if org_length != tr_length:
        return False
    # Check if all keys in the original are present in the translation
    for key in original_sections:
        if key not in translated_sections:
            return False
    return True


def split_srt_string(srt_string, max_length=4096):
    """
    Splits an SRT string into chunks, ensuring full subtitle blocks are preserved.

    Args:
        srt_string (str): The input SRT string.
        max_length (int): The maximum length of each chunk.

    Returns:
        list: A list of SRT chunks, each not exceeding max_length.
    """
    chunks = []
    current_chunk = ""
    current_length = 0

    # Split the SRT string into blocks (split by double newlines)
    blocks = srt_string.strip().split('\n\n')

    for block in blocks:
        block += '\n\n'  # Add back the double newline to preserve format
        block_length = len(block)

        # Check if adding this block exceeds the max_length
        if current_length + block_length > max_length:
            # Save the current chunk and start a new one
            chunks.append(current_chunk.strip())
            current_chunk = block
            current_length = block_length
        else:
            # Add the block to the current chunk
            current_chunk += block
            current_length += block_length

    # Add the last chunk if it has content
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    return chunks


def send_request(llm, request, content, log,start_time):
    parts = split_srt_string(content, 4096 - len(request))  # split file, max_length is 4096 per request
    full_res = ''
    counter = 0
    for part in parts:
        counter += 1
        if log:
            print('=========================================')
            print(part[:100])
            print('------------------------------')
            print(part[-100:])
            print('=========================================')

        while True:
            # send request, put main content in ``, remove useless symbol
            try:
                response = llm.invoke(request + f"`\n{part}\n`")
            except Exception as e:
                return False

            half_res = response.content.replace('`', '').replace('srt', '', 1)  # delete description and symbols
            if check_translate(part, half_res):
                full_res += ('\n\n' + half_res)  # save them in main text
                break
            print(f'\n\rSome data lost, try again...',end="")
        if not log:
            percentage_complete=(counter/len(parts))*100
            print(f"\r{percentage_complete:.2f}% Combleted translation part{counter} Completed...",end="")
    return full_res


def reader(en_path):
    with open(en_path, 'r',encoding="utf-8-sig") as f:  # Read english file
        return ''.join(f.readlines())


def writer(content, export_dir, filename):
    fa_path = export_dir + "/" + f"tr.{filename}"  # create new fa file path
    with open(fa_path, 'w',encoding="utf-8") as f:
        f.write(content)


def translator(source_dir, export_dir, base_url, api_key, model_name, lang, conversational=False, log=False, delete=True):
    llm = ChatOpenAI(
        base_url=base_url,
        model=model_name,
        api_key=api_key,
    )
    sub_titles = []
    for _, _, filenames in walk(source_dir):  # get source files
        sub_titles.extend(filenames)
        break

    if conversational:
        conversational = '`conversational`'
    else:
        conversational = ''

    for item in sub_titles:
        old_request = f"""
        help me to translate some .srt text to {conversational} {lang},
        as response only write the result (without any symbol),
        remember we need number and times in text to make .srt file,
        don't combine two parts and take care of their time,
        make sure to not lose any translation,
        also don't add or remove anything from text,
        I put the text in `` and the text:\n
        """

        request = f"""
        convert these subtitles in {conversational} {lang} but , i don't mean just translation ,
        you should understand consept of text and rewrite it by yourself. 
        focus on the concepts and making the translation natural , meaningful and fluent.
        I put the text in `` , just give the result and Don't add a part to the translation , their format is .srt:
        """

        en_path = f"{source_dir}/{item}"
        content = reader(en_path=en_path)
        start_time = time.time()  # to calculate run time
        full_res = send_request(llm=llm, request=request, content=content, log=log,start_time=start_time)
        if not full_res:
            print("Well, Network in not connected or You reached maximum request per day...")
            return

        print("%s seconds" % (time.time() - start_time))  # to calculate run time
        writer(content=full_res, export_dir=export_dir, filename=item)
        if delete:
            Path.unlink(Path(en_path))  # delete fa file
        print(f">>>> {item} finished <<<<")


source_dir = os.getenv('SOURCE_DIR')
export_dir = os.getenv('EXPORT_DIR')
base_url = os.getenv('BASE_URL')
api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API_KEY is required but not set.")
model_name = os.getenv('MODEL_NAME') or "gpt-4o-mini"
lang = os.getenv('LANGUAGE') or 'persian'
conversational = bool(os.getenv('CONVERSATIONAL')) or True

if __name__ == "__main__":
    translator(
        source_dir=source_dir,
        export_dir=export_dir,
        base_url=base_url,
        api_key=api_key,
        model_name=model_name,
        conversational=conversational,
        lang=lang,
        delete=True,
    )
