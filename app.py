import streamlit as st
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="Abdo Farag AI Studio", page_icon="💎", layout="centered")

# تنسيق الموبايل والخطوط (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    h1, h2, h3 { color: #FFD700 !important; text-align: center; }
    p { color: white !important; text-align: center; font-size: 18px; }
    /* تنسيق الزرار عشان يبان بوضوح */
    .stButton>button {
        width: 100%;
        background-color: #FFD700 !important;
        color: black !important;
        font-weight: bold !important;
        height: 3em;
        border-radius: 10px;
    }
    /* تنسيق خانة الكتابة */
    .stTextInput>div>div>input {
        background-color: #1A1C23 !important;
        color: white !important;
        border: 1px solid #FFD700 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 ABDO FARAG AI STUDIO")
st.markdown("<p>The Masterpiece Prompt Generator</p>", unsafe_allow_html=True)

# خانة الإدخال
user_input = st.text_input("Enter your creative idea here:", placeholder="e.g. A lion wearing a golden crown")

if st.button("GENERATE IMAGE ✨"):
    if user_input:
        st.markdown("---")
        # رابط الصورة المباشر (أسرع واحد في العالم)
        clean_text = urllib.parse.quote(user_input)
        image_url = f"https://image.pollinations.ai/prompt/{clean_text}?width=1024&height=1024&nologo=true"
        
        # عرض الصورة
        st.image(image_url, caption="Your AI Masterpiece", use_container_width=True)
        
        # عرض البرومبت تحتها
        st.subheader("📝 Professional Prompt:")
        st.code(f"Cinematic shot of {user_input}, hyper-realistic, 8k, luxury lighting")
    else:
        st.warning("Please type your idea first!")

st.markdown("---")
st.markdown("<p>Created by: Abdo Farag | AI Content Creator & Developer</p>", unsafe_allow_html=True)
