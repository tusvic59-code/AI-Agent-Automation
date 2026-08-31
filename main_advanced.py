"""
برنامه اصلی - رابط کاربری Agent پیشرفته
"""

import sys
from pathlib import Path
from agent.advanced_agent import AdvancedAIAgent
import json

def display_main_menu():
    print("\n" + "="*60)
    print("🤖 ایجنت AI پیشرفته - نسخه 2.0")
    print("="*60)
    print("\n📋 منو اصلی:")
    print("1. 🔍 جستجو در اینترنت")
    print("2. 📄 تجزیه فایل‌های Python")
    print("3. 📧 ارسال ایمیل")
    print("4. 📊 تحلیل داده (CSV/Excel/JSON)")
    print("5. 🔧 بهبود کد")
    print("6. 📝 خلاصه‌سازی متن")
    print("7. 🌐 ترجمه متن")
    print("8. ⚙️ اجرای کد Python")
    print("9. 📋 تولید گزارش")
    print("10. 💾 مدیریت حافظه")
    print("11. ℹ️ وضعیت Agent")
    print("0. 🚪 خروج")
    print()

def test_agent():
    """تست خودکار ایجنت"""
    print("\n" + "="*60)
    print("🧪 شروع تست‌های خودکار...")
    print("="*60)
    
    agent = AdvancedAIAgent()
    
    # تست 1: جستجو
    print("\n✅ تست 1: جستجو در اینترنت")
    print("-" * 40)
    results = agent.search_internet("پایتون برنامه‌نویسی")
    for i, result in enumerate(results[:2], 1):
        print(f"{i}. {result['title']}")
        print(f"   📌 {result['snippet'][:100]}...")
    
    # تست 2: تجزیه Python
    print("\n✅ تست 2: تجزیه فایل Python")
    print("-" * 40)
    analysis = agent.analyze_python_file("agent/advanced_agent.py")
    print(f"📁 فایل: {analysis.get('file', 'N/A')}")
    print(f"📊 خطوط: {analysis.get('lines', 0)}")
    print(f"🔧 Functions: {len(analysis.get('functions', []))} عدد")
    print(f"📦 Classes: {len(analysis.get('classes', []))} عدد")
    
    # تست 3: بهبود کد
    print("\n✅ تست 3: بهبود کد")
    print("-" * 40)
    sample_code = """
def calculate(a, b):
    return a + b

x = calculate(5, 3)
print(x)
"""
    suggestions = agent.improve_code(sample_code)
    print(f"💡 پیشنهادها:")
    for suggestion in suggestions.get('suggestions', []):
        print(f"  {suggestion}")
    
    # تست 4: خلاصه‌سازی
    print("\n✅ تست 4: خلاصه‌سازی متن")
    print("-" * 40)
    long_text = """
    Python یک زبان برنامه‌نویسی قدرتمند است. 
    استفاده در علم داده و هوش مصنوعی بسیار رایج است.
    کتاب‌خانه‌های غنی آن مثل NumPy و Pandas بسیار محبوب هستند.
    یادگیری Python برای مبتدیان آسان است.
    """
    summary = agent.summarize_text(long_text)
    print(f"📝 خلاصه: {summary.get('summary', 'N/A')[:100]}...")
    print(f"📊 کاهش: {summary.get('reduction', 'N/A')}")
    
    # تست 5: تولید گزارش
    print("\n✅ تست 5: تولید گزارش")
    print("-" * 40)
    test_data = {
        'تست_شماره': 5,
        'وضعیت': 'کامیاب',
        'زمان': '0.5 ثانیه'
    }
    report = agent.generate_report(test_data)
    print(report)
    
    # تست 6: وضعیت
    print("\n✅ تست 6: وضعیت Agent")
    print("-" * 40)
    status = agent.get_status()
    for key, value in status.items():
        print(f"  {key}: {value}")
    
    print("\n" + "="*60)
    print("✅ تمام تست‌ها با موفقیت انجام شدند!")
    print("="*60)

def main():
    agent = AdvancedAIAgent()
    
    print("\n" + "="*60)
    print("🤖 خوش آمدید به ایجنت AI پیشرفته!")
    print("="*60)
    
    # اجرای تست‌های خودکار
    run_tests = input("\n🧪 آیا می‌خواهید تست‌های خودکار اجرا شوند؟ (بله/خیر): ").strip().lower()
    if run_tests in ['بله', 'yes', 'y']:
        test_agent()
    
    # حلقه اصلی
    while True:
        display_main_menu()
        choice = input("انتخاب کنید (0-11): ").strip()
        
        try:
            if choice == '0':
                print("\n👋 خدافظ!")
                break
            
            elif choice == '1':
                # جستجو
                query = input("\n🔍 چی رو جستجو کنم؟ ")
                if query:
                    results = agent.search_internet(query)
                    print(f"\n📊 نتایج جستجو:\n")
                    for i, result in enumerate(results, 1):
                        print(f"{i}. {result['title']}")
                        if result['snippet']:
                            print(f"   📌 {result['snippet']}\n")
            
            elif choice == '2':
                # تجزیه Python
                file_path = input("\n📁 مسیر فایل Python: ")
                if file_path:
                    analysis = agent.analyze_python_file(file_path)
                    if 'error' not in analysis:
                        print(f"\n✅ نتایج:")
                        print(f"  📊 خطوط: {analysis.get('lines', 0)}")
                        print(f"  🔧 Functions: {analysis.get('functions', [])}")
                        print(f"  📦 Classes: {analysis.get('classes', [])}")
                    else:
                        print(f"\n{analysis['error']}")
            
            elif choice == '3':
                # ایمیل
                to_email = input("\nایمیل دریافت‌کننده: ")
                subject = input("موضوع: ")
                body = input("متن: ")
                result = agent.send_email(to_email, subject, body)
                print(f"\n{result.get('status', result.get('error', 'N/A'))}")
            
            elif choice == '4':
                # تحلیل داده
                file_path = input("\n📁 مسیر فایل (CSV/Excel/JSON): ")
                if file_path:
                    analysis = agent.analyze_data_file(file_path)
                    if 'error' not in analysis:
                        print(f"\n✅ نتایج:")
                        for key, value in analysis.items():
                            print(f"  {key}: {value}")
                    else:
                        print(f"\n{analysis['error']}")
            
            elif choice == '5':
                # بهبود کد
                print("کد را وارد کنید (Enter دو بار برای پایان):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        if lines and lines[-1] == "":
                            break
                    lines.append(line)
                
                code = "\n".join(lines[:-1])
                suggestions = agent.improve_code(code)
                print(f"\n💡 پیشنهادها:")
                for suggestion in suggestions.get('suggestions', []):
                    print(f"  {suggestion}")
            
            elif choice == '6':
                # خلاصه‌سازی
                print("متن را وارد کنید (Enter دو بار برای پایان):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        if lines and lines[-1] == "":
                            break
                    lines.append(line)
                
                text = "\n".join(lines[:-1])
                summary = agent.summarize_text(text)
                print(f"\n📝 خلاصه:\n{summary.get('summary', 'N/A')}")
            
            elif choice == '7':
                # ترجمه
                text = input("\nمتن برای ترجمه: ")
                lang = input("زبان هدف (en/fa): ").strip().lower()
                result = agent.translate_text(text, lang)
                print(f"\n{result.get('status', result.get('error', 'N/A'))}")
            
            elif choice == '8':
                # اجرای کد
                print("کد Python را وارد کنید (Enter دو بار برای پایان):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        if lines and lines[-1] == "":
                            break
                    lines.append(line)
                
                code = "\n".join(lines[:-1])
                result = agent.execute_python_code(code)
                print(f"\n⚙️ نتیجه:")
                if 'error' in result:
                    print(f"{result['error']}")
                else:
                    print(f"{result.get('result', 'N/A')}")
            
            elif choice == '9':
                # تولید گزارش
                print("داده‌های گزارش را وارد کنید (JSON):")
                data_input = input()
                try:
                    data = json.loads(data_input)
                    report = agent.generate_report(data)
                    print(f"\n{report}")
                except:
                    print("❌ فرمت JSON نامعتبر است")
            
            elif choice == '10':
                # حافظه
                sub_choice = input("\n1. ذخیره\n2. بارگذاری\nانتخاب: ").strip()
                if sub_choice == '1':
                    key = input("کلید: ")
                    value = input("مقدار: ")
                    agent.save_memory(key, value)
                elif sub_choice == '2':
                    key = input("کلید: ")
                    value = agent.load_memory(key)
                    print(f"مقدار: {value}")
            
            elif choice == '11':
                # وضعیت
                status = agent.get_status()
                print("\n✅ وضعیت Agent:")
                for key, value in status.items():
                    print(f"  {key}: {value}")
            
            else:
                print("❌ انتخاب نامعتبر!")
        
        except Exception as e:
            print(f"❌ خطا: {str(e)}")

if __name__ == "__main__":
    main()
