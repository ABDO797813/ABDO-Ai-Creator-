import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة عشان تبان احترافية
st.set_page_config(page_title="Abdo Farag AI Studio", page_icon="🎨", layout="centered")

# 2. تنسيق الكلام عشان يبان بوضوح (CSS بسيط)
st.markdown("""
    <style>
    .main { text-align: center; }
    h1 { color: #FF4B4B; font-size: 50px !important; }
    h3 { color: #31333F; font-size: 30px !important; }
    .stTextInput label { font-size: 20px !important; font-weight: bold; }
    </style>
    """, unsafe_allow_ Harris=True)

st.title("🎨 Abdo Farag AI Studio")
st.markdown("### 🚀 Automated Storyboard Generator")

# 3. إدخال البيانات
user_input = st.text_input("What do you want to create? (Write here):")

if st.button("Generate Magic ✨"):
    if user_input:
        st.markdown("---")
        
        # عرض البرومبت بشكل شيك
        st.subheader("📝 Your Professional Prompt:")
        st.info(f"Hyper-realistic cinematic shot of {user_input}, 8k, luxury lighting")
        
        # 4. حل مشكلة الصورة (رابط مباشر وسريع جداً)
        st.markdown("### 🖼️ AI Generated Preview:")
        
        # تنظيف النص واستخدام سيرفر صور مختلف ومضمون
        clean_text = urllib.parse.quote(user_input)
        image_url = f"https://image.pollinations.ai/prompt/{clean_text}?width=1024&height=1024&nologo=true"
        
        # عرض الصورة
        st.image(image_url, caption=f"Preview for: {user_input}", use_container_width=True)
        
        st.success("Your image is ready! 🚀")
    else:
        st.warning("Please type something first!")

st.markdown("---")
st.caption("© 2026 Abdo Farag AI Studio | Designed for Mobile & Web")
