"""
🤖 AI Agent - خودکارسازی و تجزیه‌وتحلیل داده‌ها
یک ایجنت هوشمند برای انجام کارهای خودکار
"""

import os
import sys
from pathlib import Path

# اضافه کردن مسیر پروژه
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from agent.core import AIAgent
from agent.ui import run_ui

def main():
    """تابع اصلی برنامه"""
    print("=" * 60)
    print("🤖 خوش آمدید به AI Agent - خودکارسازی و تجزیه‌وتحلیل")
    print("=" * 60)
    print()
    
    # ایجاد ایجنت
    agent = AIAgent()
    
    # نمایش منو
    while True:
        print("\n📋 منو:")
        print("1. چت با ایجنت")
        print("2. جستجو در اینترنت")
        print("3. تجزیه‌وتحلیل فایل")
        print("4. خروج")
        
        choice = input("\nانتخاب کنید (1-4): ").strip()
        
        if choice == "1":
            user_input = input("\n💬 دستور خود را وارد کنید: ").strip()
            if user_input:
                response = agent.process_command(user_input)
                print(f"\n🤖 ایجنت: {response}")
        
        elif choice == "2":
            query = input("\n🔍 چی رو جستجو کنم؟ ").strip()
            if query:
                results = agent.search_internet(query)
                print(f"\n📊 نتایج جستجو:")
                for i, result in enumerate(results[:5], 1):
                    print(f"{i}. {result['title']}\n   {result['link']}")
        
        elif choice == "3":
            file_path = input("\n📁 مسیر فایل: ").strip()
            if os.path.exists(file_path):
                analysis = agent.analyze_file(file_path)
                print(f"\n📈 تجزیه‌وتحلیل:\n{analysis}")
            else:
                print("❌ فایل یافت نشد!")
        
        elif choice == "4":
            print("\n👋 خداحافظ!")
            break
        
        else:
            print("❌ انتخاب نامعتبر!")

if __name__ == "__main__":
    main()
