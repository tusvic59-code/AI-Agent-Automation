# 📖 نحوه استفاده

## دستورات اصلی

### 1. جستجو در اینترنت

```
جستجو برای: Python آموزش
```

ایجنت از Google جستجو می‌کند و نتایج را نشان می‌دهد.

### 2. تجزیه‌وتحلیل فایل‌ها

```
فایل.csv را تحلیل کن
```

فایل‌های پشتیبانی شده:
- CSV
- Excel (.xlsx)
- JSON
- متن معمولی

### 3. ارسال ایمیل

```
ایمیل بفرست به: test@example.com
موضوع: سلام
متن: این یک تست است
```

### 4. خودکارسازی کارها

```
هر روز ساعت 9 صبح این کار را انجام بده
```

## مثال‌های عملی

### مثال 1: جمع‌آوری اطلاعات

```python
from agent.core import AIAgent

agent = AIAgent()
results = agent.search_internet("آخرین اخبار تکنولوژی")

for result in results[:5]:
    print(f"- {result['title']}")
    print(f"  {result['link']}\n")
```

### مثال 2: تجزیه‌وتحلیل داده‌ها

```python
agent = AIAgent()
analysis = agent.analyze_file("data.csv")
print(analysis)
```
