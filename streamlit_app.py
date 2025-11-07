import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# --- PAGE SETUP ---
st.set_page_config(page_title="AI Y2K Stylist Ultimate Try-On", page_icon="💅", layout="wide")

# --- CSS ---
st.markdown("""
<style>
body {background: radial-gradient(circle at 10% 20%, #1b003a, #3d0070, #ff00cc); color:#fff; font-family:'Poppins',sans-serif;}
h1,h2,h3 {text-align:center; color:#ffb6ff; text-shadow:0 0 15px #ff00ff;}
.upload-box, .input-box, .recommend-box {background-color:rgba(255,255,255,0.1); border-radius:20px; padding:25px; margin:20px auto; width:80%; text-align:center; box-shadow:0 0 25px rgba(255,0,255,0.4);}
img {border-radius:10px; margin:5px; cursor:pointer;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>💅 AI Y2K Stylist Ultimate Try-On 💄</h1>", unsafe_allow_html=True)

# --- Upload User Photo ---
uploaded_file = st.file_uploader("Upload your half-body photo:", type=["jpg","jpeg","png"])
if uploaded_file:
    user_img = Image.open(uploaded_file).convert("RGBA")
    st.image(user_img, caption="Your Photo", use_column_width=False)

    # --- User Preferences ---
    st.subheader("Customize Your Style")
    style = st.selectbox("Fashion Style:", ["Y2K","Streetwear","Cute","Minimalist","Glam"])
    budget = st.slider("Budget ($):", 50, 500, 150, step=10)
    color_pref = st.selectbox("Favorite Color:", ["Pink","Blue","Black","White","Purple","Neon Green"])

    # --- Asset Libraries (replace with your real PNGs) ---
    outfit_urls = {
        "Y2K":["https://i.ibb.co/2n7Y0kg/y2k1.png",
               "https://i.ibb.co/WsvK5jZ/y2k2.png",
               "https://i.ibb.co/fv4QH1x/y2k3.png"]
    }
    nail_urls = {
        "Y2K":["https://i.ibb.co/2KxFz5n/nail1.png",
               "https://i.ibb.co/7NvJ2xF/nail2.png",
               "https://i.ibb.co/5W1D7qK/nail3.png"]
    }
    accessory_urls = {
        "Y2K":["https://i.ibb.co/2n7Y0kg/bag1.png",
               "https://i.ibb.co/WsvK5jZ/shoes1.png",
               "https://i.ibb.co/fv4QH1x/necklace1.png"]
    }

    # --- Selection ---
    st.subheader("Select Outfit")
    outfit_choice = st.selectbox("Choose outfit:", outfit_urls[style])
    st.subheader("Select Nail Style")
    nail_choice = st.selectbox("Choose nails:", nail_urls[style])
    st.subheader("Select Accessory")
    accessory_choice = st.selectbox("Choose accessory:", accessory_urls[style])

    # --- Load Images ---
    def load_image(url):
        response = requests.get(url)
        return Image.open(BytesIO(response.content)).convert("RGBA")

    outfit_img = load_image(outfit_choice)
    nail_img = load_image(nail_choice)
    accessory_img = load_image(accessory_choice)

    # --- Compose Try-On Image ---
    combined = user_img.copy()
    combined.paste(outfit_img, (0,0), outfit_img)       # Outfit overlay
    combined.paste(nail_img, (0,0), nail_img)           # Nail overlay
    combined.paste(accessory_img, (0,0), accessory_img) # Accessory overlay

    st.subheader("👗 Your Ultimate Try-On Preview")
    st.image(combined, caption="Try-On Result", use_column_width=True)

    st.download_button(
        label="💾 Download Your Try-On Image",
        data=combined.tobytes(),
        file_name="my_tryon.png",
        mime="image/png"
    )

else:
    st.markdown('<p style="text-align:center;">Upload your photo above to start your ultimate AI fashion journey 💫</p >', unsafe_allow_html=True)
