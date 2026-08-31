"""
مثال: تجزیه‌وتحلیل داده‌ها
"""

import sys
from pathlib import Path
import pandas as pd

# اضافه کردن مسیر پروژه
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent.core import AIAgent

def main():
    # ایجاد داده نمونه
    data = {
        'نام': ['علی', 'فاطمه', 'محمد'],
        'سن': [25, 30, 28],
        'شهر': ['تهران', 'اصفهان', 'شیراز']
    }
    
    df = pd.DataFrame(data)
    df.to_csv('sample_data.csv', index=False)
    
    # تجزیه‌وتحلیل
    agent = AIAgent()
    analysis = agent.analyze_file('sample_data.csv')
    
    print("📊 تجزیه‌وتحلیل فایل:")
    print(analysis)

if __name__ == "__main__":
    main()
