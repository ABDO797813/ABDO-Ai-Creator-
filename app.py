import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Abdo Farag AI Studio", layout="wide")

# 2. كود التصميم (CSS) - النسخة المعدلة لظهور كل النصوص بوضوح
st.markdown("""
    <style>
    /* تلوين الخلفية */
    .stApp { 
        background: radial-gradient(circle, #1a1a2e 0%, #0f0f1a 100%); 
    }
    
    /* إجبار كل النصوص والفقرات والعناوين على الظهور باللون الأبيض أو الذهبي */
    .stApp p, .stApp label, .stApp span, .stApp div, .stApp h3 {
        color: #ffffff !important; 
    }

    /* تنسيق العنوان الرئيسي بالذهبي */
    .main-title { 
        text-align: center; 
        font-size: 3.5rem !important; 
        background: -webkit-linear-gradient(#FFD700, #FFA500); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        font-weight: 800;
        margin-bottom: 0px;
    }

    /* تنسيق الشريط الجانبي (Sidebar) */
    [data-testid="stSidebar"] { 
        background-color: #0b0b15 !important; 
        border-right: 2px solid #FFD700; 
    }
    
    /* نصوص الشريط الجانبي */
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] h2 {
        color: #FFD700 !important;
        font-weight: bold;
    }

    /* تنسيق أزرار الاستايلات في الجنب */
    [data-testid="stSidebar"] .stButton > button { 
        width: 100%; 
        border: 1px solid #FFD700 !important; 
        background: transparent !important; 
        color: #FFD700 !important; 
        border-radius: 10px;
        transition: 0.3s;
    }
    [data-testid="stSidebar"] .stButton > button:hover { 
        background: #FFD700 !important; 
        color: black !important; 
        box-shadow: 0 0 10px #FFD700;
    }

    /* تنسيق مربع الكتابة */
    .stTextInput input {
        background-color: #1e1e2f !important;
        color: white !important;
        border: 1px solid #3e3e42 !important;
    }

    /* تنسيق زر التوليد الرئيسي (براق) */
    .gen-btn button {
        background: linear-gradient(90deg, #FFD700, #FFA500) !important;
        color: black !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        border: none !important;
        padding: 10px 0px !important;
        width: 100%;
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الشريط الجانبي (Sidebar)
with st.sidebar:
    st.markdown("## 💎 AI PRESETS")
    st.write("Select a style to enhance your prompt:")
    
    if 'style' not in st.session_state:
        st.session_state.style = ""

    if st.button("🎬 Cinematic Mode"):
        st.session_state.style = "highly detailed, cinematic lighting, 8k, dramatic shadows, unreal engine 5 style"
    
    if st.button("🎨 Cartoon Style"):
        st.session_state.style = "3d render, pixar style, vibrant colors, cute character, high quality"
        
    if st.button("🎮 Cyberpunk"):
        st.session_state.style = "cyberpunk aesthetic, neon lights, futuristic city, high contrast, sharp details"

    if st.button("📸 Realistic Photo"):
        st.session_state.style = "photorealistic, shot on 35mm lens, raw photo, ultra detailed, 8k"

    st.write("---")
    if st.button("✨ Clear Style"):
        st.session_state.style = ""
        st.rerun()

# 4. محتوى الصفحة الرئيسي
st.markdown('<h1 class="main-title">💎 ABDO FARAG AI STUDIO 💎</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8a8a8a;'>The Masterpiece Prompt Generator</p>", unsafe_allow_html=True)

st.write("") # مسافة

user_input = st.text_input("Enter your creative idea here:", placeholder="e.g. A lion wearing a golden crown")

# عرض الاستايل المختار حالياً فوق الزر
if st.session_state.style:
    st.markdown(f"📍 **Active Style:** <span style='color:#FFD700'>{st.session_state.style.split(',')[0]}</span>", unsafe_allow_html=True)

# زر التوليد الرئيسي
st.write("")
st.markdown('<div class="gen-btn">', unsafe_allow_html=True)
if st.button("GENERATE PREMIUM PROMPT ⚡"):
    if user_input:
        final_prompt = f"{user_input}, {st.session_state.style}"
        st.markdown("### 🏆 Your Premium Prompt:")
        st.code(final_prompt)
        st.balloons() # احتفال بسيط بالنتيجة
    else:
        st.warning("Please type your idea first!")
st.markdown('</div>', unsafe_allow_html=True)

# الـ Footer
st.markdown("<br><br><br><p style='text-align: center; font-size: 0.8rem; color: #555;'>Created by: Abdo Farag | AI Content Creator & Developer</p>", unsafe_allow_html=True)