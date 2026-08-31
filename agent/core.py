"""
هسته اصلی ایجنت AI
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict, Any
import json

class AIAgent:
    """کلاس اصلی برای ایجنت AI"""
    
    def __init__(self):
        self.name = "AI Agent"
        self.history = []
    
    def process_command(self, command: str) -> str:
        """
        پردازش دستور کاربر
        """
        # اضافه کردن به تاریخچه
        self.history.append({
            'type': 'command',
            'content': command
        })
        
        # تجزیه دستور
        if 'جستجو' in command or 'search' in command.lower():
            query = command.replace('جستجو', '').replace('برای', '').strip()
            return f"می‌روم {query} را جستجو کنم..."
        
        elif 'تحلیل' in command or 'analyze' in command.lower():
            return "فایل را تحلیل می‌کنم..."
        
        elif 'ایمیل' in command or 'email' in command.lower():
            return "ایمیل را ارسال می‌کنم..."
        
        else:
            return f"دستور شما: {command}\nچگونه می‌تونم کمکتون کنم؟"
    
    def search_internet(self, query: str) -> List[Dict[str, str]]:
        """
        جستجو در اینترنت
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            # استفاده از Google search
            url = f"https://www.google.com/search?q={query}"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                results = []
                
                for g in soup.find_all('div', class_='g'):
                    title_elem = g.find('h3')
                    link_elem = g.find('a')
                    
                    if title_elem and link_elem:
                        title = title_elem.text
                        link = link_elem.get('href', '')
                        results.append({
                            'title': title,
                            'link': link
                        })
                
                return results[:10]
        
        except Exception as e:
            return [{'title': f'خطا: {str(e)}', 'link': ''}]
    
    def analyze_file(self, file_path: str) -> str:
        """
        تجزیه‌وتحلیل فایل
        """
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
                return f"فایل CSV: {df.shape[0]} سطر، {df.shape[1]} ستون\n\nآمار:\n{df.describe().to_string()}"
            
            elif file_path.endswith('.xlsx'):
                df = pd.read_excel(file_path)
                return f"فایل Excel: {df.shape[0]} سطر، {df.shape[1]} ستون\n\nآمار:\n{df.describe().to_string()}"
            
            elif file_path.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return f"فایل JSON تحلیل شد:\n{json.dumps(data, ensure_ascii=False, indent=2)[:500]}..."
            
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                return f"محتوای فایل ({len(content)} کاراکتر):\n{content[:500]}..."
        
        except Exception as e:
            return f"خطا در تجزیه فایل: {str(e)}"
    
    def get_history(self) -> List[Dict]:
        """دریافت تاریخچه دستورات"""
        return self.history