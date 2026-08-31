"""
مثال: جستجوی ساده
"""

import sys
from pathlib import Path

# اضافه کردن مسیر پروژه
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.core import AIAgent

def main():
    # ایجاد ایجنت
    agent = AIAgent()
    
    # جستجو برای چیزی
    query = "Python برنامه‌نویسی"
    print(f"🔍 جستجو برای: {query}\n")
    
    results = agent.search_internet(query)
    
    print("📊 نتایج:")
    for i, result in enumerate(results[:5], 1):
        print(f"\n{i}. {result['title']}")
        print(f"   🔗 {result['link']}")

if __name__ == "__main__":
    main()
