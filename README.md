<br>

# 🌐 Subtitle Translator (English)

This project is a tool for translating `.srt` subtitles from any language to any language. You can use this tool to process and translate subtitle files using an AI model. With this project, you will have 200 request credits **per day** to use. <br>
⚠️ **Note**: Please note that translating large subtitle files will take time, and if the file is too large, your credits may not suffice.

🔎 **Tested Languages**: The project has only been tested on "Persian" and "English" so far.

## 🛠 Prerequisites

To use this program, you will need:

1. **A GitHub account**: If you do not already have a GitHub account, first [sign up here](https://github.com).
2. **Obtain an `API Key`**: To use this tool, you need to obtain an `API Key`. You can do this through this link:

    👉 [Click here (free)](https://api.chatanywhere.org/v1/oauth/free/render)

   Once you have obtained the `API Key`, set it in the `api_key` variable.

3. **Install required packages**: Ensure all necessary packages are installed.

## 📦 Installing Packages

To install the required packages, use the following command:

<div dir='ltr'>

```bash
pip install -r requirements.txt
```
</div>

## 🚀 How to Use

1. **Set Variables**:
   In the .env file, adjust the following variables according to your needs:

   - `SOURCE_DIR`: The directory path where the input `.srt` subtitle files are located. (Default: `import` folder)
   - `EXPORT_DIR`: The directory path where the translated Persian files should be saved. (Default: `export` folder)
   - `BASE_URL`: The API URL (default value is `https://api.chatanywhere.org`).
   - `API_KEY`: The API key obtained in the previous step.
   - `MODEL_NAME`: The name of the AI model (default: `gpt-4o-mini`).
   - `LANG` : Destination language (default: `persain`)

2. **Run the Program**:
   Execute the program using the following command:

️⚠️ **Note**: : The original files will be <b>"deleted"</b> after the translation is created, so make sure to back them up.
<div dir='ltr'>

```bash
python translator.py
```
</div>

3. **Output Structure**:
   Translated files in Persian will be saved in the directory specified in the `export_dir` variable. The output filenames will be similar to the input filenames but with a `tr` prefix.

## 🧩 Code Structure

- **`parse_srt(content)`**: Converts the content of an `.srt` file into a dictionary.
- **`check_translate(original, translated)`**: Verifies that all sections of the original file are present in the translation.
- **`split_srt_string(srt_string, max_length)`**: Splits `.srt` files into smaller chunks.
- **`send_request(llm, request, content, log)`**: Sends the translation request and manages the response.
- **`reader(en_path)`**: Reads the content of the input file.
- **`writer(content, export_dir, en_filename)`**: Saves the translated content to the output directory.
- **`translator(...)`**: Manages the main translation process.

## 📜 License

This project is released under the MIT License. For more details, see the `LICENSE` file.

## 🤝 Contribution

If you are interested in contributing to this project:

1. Create a fork of the repository.
2. Apply your changes and submit a Pull Request.
3. Ensure your changes comply with the documentation and project standards.

## 🆘 Support

For support, you can contact us via the following email address:

```
addii1385@gmail.com
```
<br>

> based on [GPT API free](https://github.com/chatanywhere/GPT_API_free)
<hr>
<br>
<br>


<div dir="rtl">
<br>

#  ترجمه گر زیرنویس  🌐  (فارسی)

این پروژه یک ابزار ترجمه زیرنویس `.srt` از هر زبان به هر زبانی است. از این ابزار می‌توانید برای پردازش و ترجمه فایل‌های زیرنویس با استفاده از مدل هوش مصنوعی بهره ببرید. در این پروژه شما  200 درخواست **در روز**  اعتبار خواهید داشت که میتوانید از ان استفاده کنید. <br>
⚠️ **نکته**:
توجه داشته باشید که ترجمه زیر نویس فایل های بزرگ زمان خواهد بود و اگر فایل خیلی بزرگ باشد احتمالا اعتبار شما کافی نخواهد بود.

🔎 **زبان های تست شده**: به این نکته توجه داشته باشید پروژه تا کنون تنها بر روی زبان های " فارسی" و "انگلیسی" تست شده است.

## 🛠 پیش‌نیازها

برای استفاده از این برنامه به موارد زیر نیاز دارید:

1. **یک اکانت گیت‌هاب**: اگر هنوز اکانت گیت‌هاب ندارید، ابتدا [ثبت‌نام کنید](https://github.com).
2. **دریافت `API Key`**: برای استفاده از این ابزار باید یک `API Key` دریافت کنید. این کار از طریق این لینک امکان‌پذیر است:


    [کلیک کنید (رایگان)](https://api.chatanywhere.org/v1/oauth/free/render) 👉


   پس از دریافت `API Key`، آن را برای اجرای کد در متغیر `api_key` قرار دهید.

3. **نصب پکیج‌های مورد نیاز**: مطمئن شوید که پکیج‌های مورد نیاز نصب شده‌اند.

## نصب پکیج‌ها 📦

برای نصب پکیج‌های مورد نیاز از دستور زیر استفاده کنید:

<div dir='ltr'>

```bash
pip install -r requirements.txt
```
</div>

## نحوه استفاده 🚀

1. **تنظیم متغیرها**:
   در فایل اصلی، متغیرهای زیر را بر اساس نیاز خود تنظیم کنید:

   - `SOURCE_DIR`: مسیر پوشه‌ای که فایل‌های زیرنویس `.srt` ورودی در آن قرار دارند. ( پیش فرض پوشه `import` )
   - `EXPORT_DIR`: مسیر پوشه‌ای که فایل‌های ترجمه‌شده فارسی باید در آن ذخیره شوند. ( پیشفرض پوشه `export` )
   - `BASE_URL`: آدرس API (به‌طور پیش‌فرض مقدار آن `https://api.chatanywhere.org` تنظیم شده است).
   - `API_KEY`: کلید API که از مرحله قبل دریافت کرده‌اید.
   - `MODEL_NAME`: نام مدل هوش مصنوعی (به‌طور پیش‌فرض `gpt-4o-mini`).
   - `LANG` :  زبان مقصد پیشفرض `فارسی` است.

2. **اجرای برنامه**:
   برنامه را با دستور زیر اجرا کنید:

⚠️ **نکته**:
توجه داشته باشید که فایل های اصلی بعد از ساخت ترجمه<b>"حذف"</b>
میشوند پس حتما بکاپ بگیرید.
<div dir='ltr'>

```bash
python translator.py
```
</div>


3. **ساختار خروجی**:
   فایل‌های ترجمه‌شده به زبان فارسی در مسیر مشخص‌شده در متغیر `export_dir` ذخیره خواهند شد. نام فایل‌های خروجی مشابه فایل‌های ورودی است اما با پیشوند `tr`.

## ساختار کد 🧩

- **`parse_srt(content)`**: محتوای فایل `.srt` را به یک دیکشنری تبدیل می‌کند.
- **`check_translate(original, translated)`**: بررسی می‌کند که تمام بخش‌های فایل اصلی در ترجمه وجود دارند.
- **`split_srt_string(srt_string, max_length)`**: فایل‌های `.srt` را به بخش‌های کوچک‌تر تقسیم می‌کند.
- **`send_request(llm, request, content, log)`**: درخواست ترجمه را ارسال کرده و پاسخ را مدیریت می‌کند.
- **`reader(en_path)`**: محتوای فایل ورودی را می‌خواند.
- **`writer(content, export_dir, en_filename)`**: محتوای ترجمه‌شده را در مسیر خروجی ذخیره می‌کند.
- **`translator(...)`**: فرآیند اصلی ترجمه را مدیریت می‌کند.

## مجوز 📜

این پروژه تحت لایسنس MIT منتشر شده است. برای اطلاعات بیشتر، فایل `LICENSE` را مشاهده کنید.

## مشارکت 🤝

اگر علاقه‌مند به مشارکت در این پروژه هستید:

1. یک فورک از مخزن ایجاد کنید.
2. تغییرات خود را اعمال کرده و یک Pull Request ارسال کنید.
3. مطمئن شوید که تغییرات شما با مستندات و استانداردهای پروژه همخوانی دارند.

## 🆘 پشتیبانی

برای پشتیبانی می‌توانید از طریق آدرس ایمیل زیر با ما در تماس باشید:

```
addii1385@gmail.com
```
<br>

> برپایه :  [GPT API free](https://github.com/chatanywhere/GPT_API_free)

<hr>
</div>
