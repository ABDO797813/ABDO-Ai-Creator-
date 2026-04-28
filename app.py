import streamlit as st
import urllib.parse

st.set_page_config(page_title="Abdo Farag AI Studio", page_icon="🎨")
st.title("🎨 Abdo Farag AI Studio")
st.markdown("### Automated Storyboard & Image Generator")

user_input = st.text_input("Describe your idea (e.g., Luxury watch, Fast car):")

if st.button("Generate Magic ✨"):
    if user_input:
        full_prompt = f"Hyper-realistic cinematic shot of {user_input}, 8k, luxury atmosphere"
        st.markdown("---")
        st.markdown("### 📝 Your Professional Prompt:")
        st.code(full_prompt)
        
        st.markdown("### 🖼️ AI Generated Preview:")
        clean_prompt = urllib.parse.quote(user_input)
        image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}"
        
        st.image(image_url, caption=f"Preview for: {user_input}")
        st.success("Success! Preview loaded.")
    else:
        st.warning("Please enter an idea first!")

st.markdown("---")
st.caption("© 2026 Abdo Farag AI Studio")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
