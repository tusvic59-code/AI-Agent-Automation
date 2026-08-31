"""
فایل تست خودکار - Unit Tests
"""

import unittest
from agent.advanced_agent import AdvancedAIAgent

class TestAdvancedAgent(unittest.TestCase):
    """تست‌های واحد برای ایجنت"""
    
    def setUp(self):
        """آماده‌سازی قبل از هر تست"""
        self.agent = AdvancedAIAgent()
    
    # تست 1: جستجو
    def test_search_internet(self):
        """تست جستجو در اینترنت"""
        print("\n✅ تست 1: جستجو در اینترنت")
        results = self.agent.search_internet("Python programming")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        print(f"   ✓ یافت شد: {len(results)} نتیجه")
    
    # تست 2: تجزیه Python
    def test_analyze_python(self):
        """تست تجزیه فایل Python"""
        print("\n✅ تست 2: تجزیه فایل Python")
        # ایجاد فایل تست موقتی
        test_code = """
def hello():
    '''Test function'''
    print('Hello')

class TestClass:
    pass
"""
        with open('test_file.py', 'w') as f:
            f.write(test_code)
        
        analysis = self.agent.analyze_python_file('test_file.py')
        self.assertIn('functions', analysis)
        self.assertIn('classes', analysis)
        print(f"   ✓ شناسایی شد: {len(analysis['functions'])} تابع")
        
        # پاک‌کردن فایل تست
        import os
        os.remove('test_file.py')
    
    # تست 3: بهبود کد
    def test_improve_code(self):
        """تست بهبود کد"""
        print("\n✅ تست 3: بهبود کد")
        code = "x = 5\ny = 10\nprint(x + y)"
        suggestions = self.agent.improve_code(code)
        self.assertIn('suggestions', suggestions)
        print(f"   ✓ پیشنهادات: {len(suggestions['suggestions'])}")
    
    # تست 4: خلاصه‌سازی
    def test_summarize(self):
        """تست خلاصه‌سازی متن"""
        print("\n✅ تست 4: خلاصه‌سازی متن")
        text = "Python is a programming language. " * 10
        summary = self.agent.summarize_text(text)
        self.assertIn('summary', summary)
        self.assertLess(len(summary['summary']), len(text))
        print(f"   ✓ کاهش: {summary.get('reduction', 'N/A')}")
    
    # تست 5: تولید گزارش
    def test_generate_report(self):
        """تست تولید گزارش"""
        print("\n✅ تست 5: تولید گزارش")
        data = {'test': 'data', 'value': 123}
        report = self.agent.generate_report(data)
        self.assertIsInstance(report, str)
        self.assertIn('گزارش', report)
        print(f"   ✓ گزارش تولید شد")
    
    # تست 6: حافظه
    def test_memory(self):
        """تست سیستم حافظه"""
        print("\n✅ تست 6: سیستم حافظه")
        self.agent.save_memory('test_key', 'test_value')
        value = self.agent.load_memory('test_key')
        self.assertEqual(value, 'test_value')
        print(f"   ✓ ذخیره و بارگذاری موفق")
    
    # تست 7: وضعیت
    def test_status(self):
        """تست وضعیت Agent"""
        print("\n✅ تست 7: وضعیت Agent")
        status = self.agent.get_status()
        self.assertIn('status', status)
        self.assertEqual(status['status'], '✅ آماده')
        print(f"   ✓ وضعیت: {status['status']}")

def run_all_tests():
    """اجرای تمام تست‌ها"""
    print("\n" + "="*60)
    print("🧪 اجرای تمام تست‌های واحد")
    print("="*60)
    
    # ایجاد suite تست
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAdvancedAgent)
    
    # اجرای تست‌ها
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # خلاصه
    print("\n" + "="*60)
    print(f"✅ تست‌های موفق: {result.testsRun - len(result.failures)}/{result.testsRun}")
    print(f"❌ تست‌های ناموفق: {len(result.failures)}")
    print("="*60)
    
    return result.wasSuccessful()

if __name__ == '__main__':
    run_all_tests()
