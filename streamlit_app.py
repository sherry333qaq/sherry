import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# --- Page Config ---
st.set_page_config(page_title="AI Y2K Stylist Ultimate Try-On", page_icon="💅", layout="wide")

# --- CSS ---
st.markdown("""
<style>
body {background: radial-gradient(circle at 10% 20%, #1b003a, #3d0070, #ff00cc); color:#fff; font-family:'Poppins',sans-serif;}
h1,h2,h3 {text-align:center; color:#ffb6ff; text-shadow:0 0 15px #ff00ff;}
.container {display: flex; flex-wrap: wrap; justify-content: center;}
.clickable-img {margin: 10px; border-radius: 10px; cursor: pointer; width:150px;}
.footer {text-align:center; color:#ffb6ff; margin-top:50px;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>💅 AI Y2K Stylist Ultimate Try-On 💄</h1>", unsafe_allow_html=True)

# --- Upload Photo ---
uploaded_file = st.file_uploader("Upload your half-body photo:", type=["jpg","jpeg","png"])
if uploaded_file:
    user_img = Image.open(uploaded_file).convert("RGBA")
    st.image(user_img, caption="Your Photo", use_column_width=False)

    # --- Preferences ---
    st.subheader("Style Preferences")
    style = st.selectbox("Fashion Style:", ["Y2K","Streetwear","Cute","Minimalist","Glam"])
    color_pref = st.selectbox("Favorite Color:", ["Pink","Blue","Black","White","Purple","Neon Green"])
    budget = st.slider("Budget ($):", 50, 500, 150, step=10)

    # --- Mock Assets (replace with your PNGs) ---
    outfit_urls = ["https://i.ibb.co/2n7Y0kg/y2k1.png",
                   "https://i.ibb.co/WsvK5jZ/y2k2.png",
                   "https://i.ibb.co/fv4QH1x/y2k3.png"]
    nail_urls = ["https://i.ibb.co/2KxFz5n/nail1.png",
                 "https://i.ibb.co/7NvJ2xF/nail2.png",
                 "https://i.ibb.co/5W1D7qK/nail3.png"]
    accessory_urls = ["https://i.ibb.co/2n7Y0kg/bag1.png",
                      "https://i.ibb.co/WsvK5jZ/shoes1.png",
                      "https://i.ibb.co/fv4QH1x/necklace1.png"]

    def load_image(url):
        response = requests.get(url)
        return Image.open(BytesIO(response.content)).convert("RGBA")

    # --- Display clickable outfits ---
    st.subheader("Select Outfit")
    outfit_choice = None
    cols = st.columns(len(outfit_urls))
    for i, url in enumerate(outfit_urls):
        with cols[i]:
            img = load_image(url)
            if st.button("", key=f"outfit_{i}"):
                outfit_choice = img
            st.image(img, use_column_width=True)

    st.subheader("Select Nail Style")
    nail_choice = None
    cols = st.columns(len(nail_urls))
    for i, url in enumerate(nail_urls):
        with cols[i]:
            img = load_image(url)
            if st.button("", key=f"nail_{i}"):
                nail_choice = img
            st.image(img, use_column_width=True)

    st.subheader("Select Accessory")
    accessory_choice = None
    cols = st.columns(len(accessory_urls))
    for i, url in enumerate(accessory_urls):
        with cols[i]:
            img = load_image(url)
            if st.button("", key=f"acc_{i}"):
                accessory_choice = img
            st.image(img, use_column_width=True)

    # --- Compose final image ---
    if outfit_choice or nail_choice or accessory_choice:
        combined = user_img.copy()
        if outfit_choice: combined.paste(outfit_choice, (0,0), outfit_choice)
        if nail_choice: combined.paste(nail_choice, (0,0), nail_choice)
        if accessory_choice: combined.paste(accessory_choice, (0,0), accessory_choice)
        st.subheader("👗 Your Try-On Preview")
        st.image(combined, use_column_width=True)
        st.download_button(
            label="💾 Download Your Try-On Image",
            data=combined.tobytes(),
            file_name="my_tryon.png",
            mime="image/png"
        )

# --- Footer with signature ---
st.markdown("""
<div class="footer">
<hr>
<p>Sherry | Business Cooperation: tuxr2021@163.com | Support Originality</p >
</div>
""", unsafe_allow_html=True)

else:
    st.markdown('<p style="text-align:center;">Upload your photo above to start your ultimate AI fashion try-on 💫</p >', unsafe_allow_html=True)
