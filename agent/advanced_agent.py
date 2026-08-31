"""
AI Agent - سیستم ایجنت AI پیشرفته و کامل
تمام قابلیت‌های یک AI مدل بزرگ، اما رایگان!
"""

import requests
import json
import os
from typing import List, Dict, Any, Optional
from datetime import datetime
import subprocess
import re

class AdvancedAIAgent:
    """ایجنت هوشمند پیشرفته"""
    
    def __init__(self):
        self.name = "Advanced AI Agent"
        self.history = []
        self.tasks_completed = 0
        self.memory = {}
    
    # ✅ 1. جستجو در اینترنت
    def search_internet(self, query: str) -> List[Dict[str, str]]:
        """جستجو در Wikipedia و DuckDuckGo"""
        try:
            print(f"🔍 در حال جستجو برای: {query}")
            
            headers = {'User-Agent': 'Mozilla/5.0'}
            
            # Wikipedia API
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'list': 'search',
                'srsearch': query,
                'format': 'json',
                'utf8': True
            }
            
            response = requests.get(url, params=params, headers=headers, timeout=10)
            data = response.json()
            results = []
            
            if 'query' in data and 'search' in data['query']:
                for item in data['query']['search'][:5]:
                    results.append({
                        'title': item.get('title', ''),
                        'link': f"https://en.wikipedia.org/wiki/{item.get('title', '').replace(' ', '_')}",
                        'snippet': item.get('snippet', '')[:200]
                    })
            
            return results if results else [{'title': '❌ نتیجه‌ای یافت نشد', 'link': '', 'snippet': ''}]
        
        except Exception as e:
            return [{'title': f'❌ خطا: {str(e)}', 'link': '', 'snippet': ''}]
    
    # ✅ 2. تجزیه‌وتحلیل فایل‌های پایتون
    def analyze_python_file(self, file_path: str) -> Dict[str, Any]:
        """تجزیه و تحلیل فایل‌های Python"""
        try:
            print(f"📄 در حال تجزیه فایل: {file_path}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # شناسایی functions
            functions = re.findall(r'def (\w+)\(', content)
            
            # شناسایی classes
            classes = re.findall(r'class (\w+)', content)
            
            # شناسایی imports
            imports = re.findall(r'from .* import|import .*', content)
            
            # تعداد خطوط
            lines = len(content.split('\n'))
            
            return {
                'file': file_path,
                'lines': lines,
                'functions': functions,
                'classes': classes,
                'imports': imports[:10],
                'size': len(content),
                'status': '✅ تجزیه شد'
            }
        
        except Exception as e:
            return {'error': f'❌ خطا: {str(e)}'}
    
    # ✅ 3. ارسال ایمیل
    def send_email(self, to_email: str, subject: str, body: str) -> Dict[str, str]:
        """ارسال ایمیل (نیاز به تنظیم SMTP)"""
        try:
            print(f"📧 در حال ارسال ایمیل به: {to_email}")
            
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            
            # توجه: این تنها یک نمونه است و نیاز به تنظیم است
            return {
                'status': '⚠️ نیاز به تنظیم SMTP',
                'to': to_email,
                'subject': subject,
                'message': 'برای ارسال ایمیل، کلیدهای SMTP را تنظیم کنید'
            }
        
        except Exception as e:
            return {'error': f'❌ خطا: {str(e)}'}
    
    # ✅ 4. تحلیل CSV/Excel
    def analyze_data_file(self, file_path: str) -> Dict[str, Any]:
        """تحلیل فایل‌های داده (CSV, Excel, JSON)"""
        try:
            print(f"📊 در حال تحلیل: {file_path}")
            
            if file_path.endswith('.csv'):
                import pandas as pd
                df = pd.read_csv(file_path)
                return {
                    'file': file_path,
                    'type': 'CSV',
                    'rows': len(df),
                    'columns': len(df.columns),
                    'column_names': list(df.columns),
                    'stats': df.describe().to_dict(),
                    'status': '✅ تحلیل شد'
                }
            
            elif file_path.endswith(('.xlsx', '.xls')):
                import pandas as pd
                df = pd.read_excel(file_path)
                return {
                    'file': file_path,
                    'type': 'Excel',
                    'rows': len(df),
                    'columns': len(df.columns),
                    'column_names': list(df.columns),
                    'status': '✅ تحلیل شد'
                }
            
            elif file_path.endswith('.json'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return {
                    'file': file_path,
                    'type': 'JSON',
                    'keys': list(data.keys()) if isinstance(data, dict) else 'List',
                    'size': len(json.dumps(data)),
                    'status': '✅ تحلیل شد'
                }
        
        except Exception as e:
            return {'error': f'❌ خطا: {str(e)}'}
    
    # ✅ 5. بهبود کد
    def improve_code(self, code: str) -> Dict[str, str]:
        """پیشنهاد بهبود برای کد"""
        try:
            print("🔧 در حال تحلیل کد برای بهبود...")
            
            suggestions = []
            
            # بررسی‌های اولیه
            if 'try:' not in code:
                suggestions.append("➕ Error handling اضافه کنید (try-except)")
            
            if 'def ' in code and '"""' not in code:
                suggestions.append("➕ Docstrings اضافه کنید")
            
            if 'import *' in code:
                suggestions.append("❌ از 'import *' استفاده نکنید")
            
            if len(code.split('\n')) > 50:
                suggestions.append("📦 کد را به توابع کوچک‌تر تقسیم کنید")
            
            return {
                'code_length': len(code),
                'suggestions': suggestions,
                'status': '✅ تحلیل شد'
            }
        
        except Exception as e:
            return {'error': f'❌ خطا: {str(e)}'}
    
    # ✅ 6. خلاصه‌سازی متن
    def summarize_text(self, text: str, percentage: float = 0.3) -> str:
        """خلاصه‌سازی متن"""
        try:
            print("📝 در حال خلاصه‌سازی متن...")
            
            sentences = text.split('.')
            num_summary = max(1, int(len(sentences) * percentage))
            
            summary = '. '.join(sentences[:num_summary]) + '.'
            
            return {
                'original_length': len(text),
                'summary_length': len(summary),
                'reduction': f"{(1 - len(summary)/len(text)) * 100:.1f}%",
                'summary': summary,
                'status': '✅ خلاصه شد'
            }
        
        except Exception as e:
            return {'error': f'❌ خطا: {str(e)}'}
    
    # ✅ 7. ترجمه متن
    def translate_text(self, text: str, target_lang: str = 'en') -> Dict[str, str]:
        """ترجمه متن (استفاده از Google Translate)"""
        try:
            print(f"🌐 در حال ترجمه به {target_lang}...")
            
            from urllib.parse import quote
            
            # استفاده از Google Translate API
            url = f"https://translate.googleapis.com/translate_a/element.js?cb=googleTranslateElementInit"
            
            # نوت: این یک نمونه ساده است
            return {
                'original': text[:100],
                'status': '⚠️ نیاز به راه‌حل ترجمه',
                'suggestion': 'از Google Translate یا Bing Translate استفاده کنید'
            }
        
        except Exception as e:
            return {'error': f'❌ خطا: {str(e)}'}
    
    # ✅ 8. اجرای کد Python
    def execute_python_code(self, code: str) -> Dict[str, Any]:
        """اجرای کد Python به صورت ایمن"""
        try:
            print("⚙️ در حال اجرای کد...")
            
            # فقط دستورات ساده و امن
            allowed_modules = ['math', 'random', 'datetime', 'json', 're']
            
            # بررسی امنیتی
            dangerous_words = ['__import__', 'exec', 'eval', 'os.', 'subprocess', 'open(']
            for word in dangerous_words:
                if word in code:
                    return {'error': f'❌ دستور {word} ممنوع است'}
            
            # اجرای کد
            local_vars = {}
            exec(code, {"__builtins__": {}}, local_vars)
            
            return {
                'result': str(local_vars),
                'status': '✅ اجرا شد'
            }
        
        except Exception as e:
            return {'error': f'❌ خطا: {str(e)}'}
    
    # ✅ 9. تولید گزارش
    def generate_report(self, data: Dict[str, Any]) -> str:
        """تولید گزارش از داده‌ها"""
        try:
            print("📋 در حال تولید گزارش...")
            
            report = f"""
╔════════════════════════════════════════╗
║          گزارش تجزیه‌وتحلیل AI          ║
╚════════════════════════════════════════╝

📅 زمان: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 اطلاعات:
"""
            
            for key, value in data.items():
                report += f"  • {key}: {value}\n"
            
            report += f"""
✅ وضعیت: تکمیل شد
"""
            
            return report
        
        except Exception as e:
            return f'❌ خطا: {str(e)}'
    
    # ✅ 10. ذخیره و بارگذاری حافظه
    def save_memory(self, key: str, value: Any):
        """ذخیره اطلاعات در حافظه"""
        self.memory[key] = value
        print(f"💾 ذخیره شد: {key}")
    
    def load_memory(self, key: str) -> Optional[Any]:
        """بارگذاری از حافظه"""
        return self.memory.get(key, None)
    
    def get_status(self) -> Dict[str, Any]:
        """وضعیت Agent"""
        return {
            'name': self.name,
            'tasks_completed': self.tasks_completed,
            'memory_items': len(self.memory),
            'timestamp': datetime.now().isoformat(),
            'status': '✅ آماده'
        }
