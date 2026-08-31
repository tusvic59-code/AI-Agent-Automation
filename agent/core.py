"""
هسته اصلی ایجنت AI
"""

import requests
from bs4 import BeautifulSoup
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
            return f"دستور شما: {command}\nچگونه می‌توانم کمکتون کنم؟"
    
    def search_internet(self, query: str) -> List[Dict[str, str]]:
        """
        جستجو در اینترنت با DuckDuckGo (بدون نیاز به API)
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            print(f"🔍 در حال جستجو برای: {query}")
            
            # استفاده از DuckDuckGo
            url = f"https://html.duckduckgo.com/?q={query}&t=h_&ia=web"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                results = []
                
                for result in soup.find_all('div', class_='result'):
                    title_elem = result.find('a', class_='result__title')
                    link_elem = result.find('a', class_='result__url')
                    
                    if title_elem and link_elem:
                        title = title_elem.get_text(strip=True)
                        link = link_elem.get('href', '')
                        
                        if title and link:
                            results.append({
                                'title': title,
                                'link': link
                            })
                
                if results:
                    return results[:10]
                else:
                    return [{'title': '❌ نتیجه‌ای یافت نشد', 'link': ''}]
            
            return [{'title': '❌ خطا در دریافت اطلاعات', 'link': ''}]
        
        except Exception as e:
            return [{'title': f'❌ خطا: {str(e)}', 'link': ''}]
    
    def analyze_file(self, file_path: str) -> str:
        """
        تجزیه‌وتحلیل فایل
        """
        try:
            if file_path.endswith('.csv'):
                try:
                    import pandas as pd
                    df = pd.read_csv(file_path)
                    return f"📊 فایل CSV: {df.shape[0]} سطر، {df.shape[1]} ستون\n\n📈 آمار:\n{df.describe().to_string()}"
                except:
                    return "⚠️ نیاز به pandas برای تجزیه CSV دارید"
            
            elif file_path.endswith('.xlsx'):
                try:
                    import pandas as pd
                    df = pd.read_excel(file_path)
                    return f"📊 فایل Excel: {df.shape[0]} سطر، {df.shape[1]} ستون\n\n📈 آمار:\n{df.describe().to_string()}"
                except:
                    return "⚠️ نیاز به pandas و openpyxl برای تجزیه Excel دارید"
            
            elif file_path.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return f"📄 فایل JSON تحلیل شد:\n{json.dumps(data, ensure_ascii=False, indent=2)[:500]}..."
            
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                return f"📝 محتوای فایل ({len(content)} کاراکتر):\n{content[:500]}..."
        
        except FileNotFoundError:
            return f"❌ فایل '{file_path}' یافت نشد"
        except Exception as e:
            return f"❌ خطا در تجزیه فایل: {str(e)}"
    
    def get_history(self) -> List[Dict]:
        """دریافت تاریخچه دستورات"""
        return self.history
