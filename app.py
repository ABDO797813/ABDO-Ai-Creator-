import streamlit as st

# Custom Styling for Luxury Look
st.set_page_config(page_title="Abdo Farag | AI Studio", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    h1 {
        color: #D4AF37; /* Gold Color */
        text-align: center;
        font-family: 'serif';
        font-weight: bold;
    }
    .stButton>button {
        background-color: #D4AF37;
        color: black;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #D4AF37;
        text-align: center;
        padding: 10px;
        font-family: 'sans-serif';
        border-top: 1px solid #D4AF37;
    }
    </style>
    """, unsafe_allow_html=True)

# Header with your Name
st.markdown("<h1>💎 ABDO FARAG AI STUDIO 💎</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: white;'>Transforming your ideas into luxury AI visual prompts.</p>", unsafe_allow_html=True)

st.markdown("---")

# Input Section
col1, col2, col3 = st.columns([1,2,1])
with col2:
    idea = st.text_input("Enter your design idea (e.g., Luxury Watch, Perfume, etc.):")
    btn = st.button("GENERATE PREMIUM PROMPT ✨")

if btn:
    if idea:
        st.markdown(f"<h3 style='color: #D4AF37;'>Masterpiece Concept: {idea}</h3>", unsafe_allow_html=True)
        luxury_prompt = f"Hyper-realistic cinematic shot of {idea}, premium product photography, elegant lighting, 8k resolution, luxury atmosphere --v 6.0"
        st.info("Your Professional AI Prompt is ready:")
        st.code(luxury_prompt)
        st.success("Copy the prompt and use it in your favorite AI image generator!")
    else:
        st.warning("Please enter an idea first, Boss.")

# Footer with your signature
st.markdown("""
    <div class="footer">
        <p>Created by: <b>Abdo Farag</b> | AI Content Creator & Designer</p>
    </div>
    """, unsafe_allow_html=True)
