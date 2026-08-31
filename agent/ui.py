"""
واسط کاربری Streamlit
"""

import streamlit as st
from .core import AIAgent

def run_ui():
    """اجرای واسط Streamlit"""
    st.set_page_config(page_title="AI Agent", layout="wide")
    
    st.title("🤖 AI Agent - خودکارسازی و تجزیه‌وتحلیل")
    st.markdown("---")
    
    # ایجاد ایجنت
    if 'agent' not in st.session_state:
        st.session_state.agent = AIAgent()
    
    agent = st.session_state.agent
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["💬 چت", "🔍 جستجو", "📊 تحلیل"])
    
    # Tab 1: Chat
    with tab1:
        st.subheader("چت با ایجنت")
        user_input = st.text_area("دستور خود را وارد کنید:")
        
        if st.button("ارسال"):
            if user_input:
                response = agent.process_command(user_input)
                st.success(f"🤖 ایجنت: {response}")
    
    # Tab 2: Search
    with tab2:
        st.subheader("جستجو در اینترنت")
        query = st.text_input("چی رو جستجو کنم؟")
        
        if st.button("جستجو کن"):
            if query:
                with st.spinner("در حال جستجو..."):
                    results = agent.search_internet(query)
                    for i, result in enumerate(results[:5], 1):
                        st.write(f"{i}. [{result['title']}]({result['link']})")
    
    # Tab 3: Analysis
    with tab3:
        st.subheader("تجزیه‌وتحلیل فایل")
        uploaded_file = st.file_uploader("فایل خود را انتخاب کنید")
        
        if uploaded_file:
            file_path = f"/tmp/{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            analysis = agent.analyze_file(file_path)
            st.write(analysis)