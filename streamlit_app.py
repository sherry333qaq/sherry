import streamlit as st
from PIL import Image
import random

# --- Page Config ---
st.set_page_config(page_title="Style Advisor", layout="wide")

# --- Y2K Pink-Black Background ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff8efb, #000000);
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Language Selection ---
language = st.sidebar.selectbox("Select Language", ["English","简体中文","日本語"])

# --- Translations Dictionary ---
translations = {
    "English": {
        "title": "Style Advisor",
        "author": "By Sherry | Business: tuxr2021@163.com",
        "step1": "Step 1: Your Info",
        "face_shape": "Face Shape",
        "skin_tone": "Skin Tone",
        "hair_color": "Hair Color",
        "favorite_colors": "Favorite Colors",
        "preferred_style": "Preferred Styles",
        "occasion": "Occasion",
        "budget": "Your Budget ($)",
        "country": "Country",
        "season": "Season",
        "step2": "Step 2: Upload Your Photo",
        "upload_photo": "Upload your photo",
        "step3": "Step 3: Generate Recommendations",
        "generate_button": "Generate Recommendations",
        "style_summary": "Style Summary",
        "footer": "I just graduated, so this project is not perfect. Please be kind and enjoy my work!"
    }
    # 可扩展其他语言
}

t = translations[language]

# --- Title ---
st.title(t["title"])
st.markdown(t["author"])

# --- User Info ---
st.sidebar.header(t["step1"])
face_shape = st.sidebar.selectbox(t["face_shape"], ["Oval","Round","Square","Heart","Diamond","Triangle","Long","Wide"])
skin_tone = st.sidebar.selectbox(t["skin_tone"], ["Cool","Warm","Neutral","Olive","Pale","Tan","Dark"])
hair_color = st.sidebar.selectbox(t["hair_color"], ["Black","Dark Brown","Light Brown","Blonde","Red","Pink","Blue","Silver","Ombre"])
favorite_colors = st.sidebar.multiselect(t["favorite_colors"], ["Red","Blue","White","Black","Pink","Green","Purple","Yellow","Orange","Silver","Gold","Neon"])
preferred_style = st.sidebar.multiselect(
    t["preferred_style"],
    ["Y2K","Asian","White Girl","HOODIE","Elegant","Casual","Streetwear","K-Pop","Indie","Girly","Grunge","Minimalist","Cute","Soft","Bold"]
)
occasion = st.sidebar.selectbox(t["occasion"], ["Class","Casual Outing","Date","Party","Work","Travel","Clubbing","Festival","Photoshoot"])
budget = st.sidebar.number_input(t["budget"], min_value=50, max_value=10000, step=50, value=200)
country = st.sidebar.selectbox(t["country"], ["China","Korea","USA","Japan","France","UK","Canada"])
season = st.sidebar.selectbox(t["season"], ["Spring","Summer","Autumn","Winter"])

# --- Upload Photo ---
st.header(t["step2"])
user_file = st.file_uploader(t["upload_photo"], type=["jpg","png"])
if user_file:
    user_image = Image.open(user_file).convert("RGBA")
    st.image(user_image, caption="Your photo", use_column_width=True)

# --- Generate Recommendations ---
st.header(t["step3"])
if st.button(t["generate_button"]):
    # Outfits by budget
    if budget >= 500:
        outfits = ["Luxury Gown", "Designer Dress", "Silk Hanfu", "Tailored Coat"]
        shoes = ["High Heels", "Designer Boots", "Platform Shoes"]
        accessories = ["Choker Necklace", "Elegant Bracelet", "Mini Designer Bag"]
    elif 200 <= budget < 500:
        outfits = ["Pleated Dress", "Mini Skirt Outfit", "Crop Top Hoodie", "Casual Jacket"]
        shoes = ["Platform Sneakers", "Chunky Boots", "Flats"]
        accessories = ["Bucket Hat", "Bracelets", "Sunglasses"]
    else:
        outfits = ["Hoodie", "T-Shirt", "Jeans", "Sweatshirt Dress"]
        shoes = ["Sneakers", "Casual Flats", "Sandals"]
        accessories = ["Simple Earrings", "Cheap Rings", "Backpack"]

    # Adjust by country & season
    if country == "China":
        outfits = [o + " (Chinese Style)" for o in outfits]
    elif country == "Korea":
        outfits = [o + " (Korean Style)" for o in outfits]

    if season == "Winter":
        outfits = [o + " + Coat" for o in outfits]
    elif season == "Summer":
        outfits = [o + " + Light Layer" for o in outfits]

    selected_outfit = random.choice(outfits)
    selected_shoes = random.choice(shoes)
    selected_accessory = random.choice(accessories)
    nails = ["Cat Eye","French Tip","Glitter","3D Decals","Ombre","Matte","Short","Long","Extensions"]
    selected_nail = random.choice(nails)

    # --- Style Summary ---
    st.subheader(t["style_summary"])
    st.write(f"Recommended Outfit: **{selected_outfit}**")
    st.write(f"Recommended Shoes: **{selected_shoes}**")
    st.write(f"Recommended Nail Style: **{selected_nail}**")
    st.write(f"Recommended Accessory: **{selected_accessory}**")
    st.write(f"Preferred Colors: {', '.join(favorite_colors) if favorite_colors else 'No preference'}")
    st.write(f"Selected Occasion: {occasion}")
    st.write(f"Your Budget: ${budget}")
    st.write(f"Country: {country} | Season: {season}")

# --- Footer ---
st.markdown("---")
st.markdown(f"<p style='text-align:center;'>{t['footer']}</p >", unsafe_allow_html=True)
