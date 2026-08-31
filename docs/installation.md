# 📖 راهنمای نصب

## پیش‌نیازها

- Python 3.9 یا بالاتر
- pip (مدیر بسته‌های Python)
- اتصال اینترنت

## مراحل نصب

### 1. دانلود پروژه

```bash
git clone https://github.com/tusvic59-code/AI-Agent-Automation.git
cd AI-Agent-Automation
```

### 2. ایجاد محیط مجازی (اختیاری اما توصیه شده)

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 3. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

## اجرا

### خط فرمان معمولی:

```bash
python main.py
```

### واسط گرافیکی (Streamlit):

```bash
streamlit run streamlit_app.py
```

## حل مشکلات

### خطا: `ModuleNotFoundError`

```bash
pip install -r requirements.txt
```

### خطا: `Permission denied`

```bash
chmod +x main.py  # فقط Mac/Linux
```
