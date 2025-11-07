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

# --- Title and Author ---
st.title("Style Advisor")
st.markdown("By Sherry | Business: tuxr2021@163.com")

# --- Sidebar: User Info ---
st.sidebar.header("Step 1: Your Info")
face_shape = st.sidebar.selectbox("Face Shape", ["Oval","Round","Square","Heart","Diamond","Triangle","Long","Wide"])
skin_tone = st.sidebar.selectbox("Skin Tone", ["Cool","Warm","Neutral","Olive","Pale","Tan","Dark"])
hair_color = st.sidebar.selectbox("Hair Color", ["Black","Dark Brown","Light Brown","Blonde","Red","Pink","Blue","Silver","Ombre"])
favorite_colors = st.sidebar.multiselect("Favorite Colors", ["Red","Blue","White","Black","Pink","Green","Purple","Yellow","Orange","Silver","Gold","Neon"])
preferred_style = st.sidebar.multiselect(
    "Preferred Styles",
    ["Y2K","Asian","White Girl","HOODIE","Elegant","Casual","Streetwear","K-Pop","Indie","Girly","Grunge","Minimalist","Cute","Soft","Bold"]
)
occasion = st.sidebar.selectbox("Occasion", ["Class","Casual Outing","Date","Party","Work","Travel","Clubbing","Festival","Photoshoot"])
budget = st.sidebar.number_input("Your Budget ($)", min_value=50, max_value=10000, step=50, value=200)
country = st.sidebar.selectbox("Country", ["China","Korea","USA","Japan","France","UK","Canada"])
season = st.sidebar.selectbox("Season", ["Spring","Summer","Autumn","Winter"])

# --- Upload Photo ---
st.header("Step 2: Upload Your Photo")
user_file = st.file_uploader("Upload your photo", type=["jpg","png"])
if user_file:
    user_image = Image.open(user_file).convert("RGBA")
    st.image(user_image, caption="Your photo", use_column_width=True)

# --- Generate Recommendations ---
st.header("Step 3: Generate Recommendations")
if st.button("Generate Recommendations"):
    # --- Outfits by Budget ---
    if budget >= 500:
        outfits = ["Luxury Gown", "Designer Dress", "Silk Hanfu", "Tailored Coat"]
        shoes = ["High Heels", "Designer Boots", "Platform Shoes"]
        accessories = ["Diamond Necklace", "Pearl Necklace", "Layered Chains", "Choker Necklace", "Elegant Bracelet", "Mini Designer Bag"]
    elif 200 <= budget < 500:
        outfits = ["Pleated Dress", "Mini Skirt Outfit", "Crop Top Hoodie", "Casual Jacket"]
        shoes = ["Platform Sneakers", "Chunky Boots", "Flats"]
        accessories = ["Bucket Hat", "Bracelets", "Sunglasses", "Charm Necklace", "Hoop Earrings"]
    else:
        outfits = ["Hoodie", "T-Shirt", "Jeans", "Sweatshirt Dress"]
        shoes = ["Sneakers", "Casual Flats", "Sandals"]
        accessories = ["Simple Earrings", "Cheap Rings", "Backpack", "Hair Clips", "Fabric Bracelet"]

    # --- Adjust by Country ---
    if country == "China":
        outfits = [o + " (Chinese Style)" for o in outfits]
    elif country == "Korea":
        outfits = [o + " (Korean Style)" for o in outfits]

    # --- Adjust by Season ---
    if season == "Winter":
        outfits = [o + " + Coat" for o in outfits]
    elif season == "Summer":
        outfits = [o + " + Light Layer" for o in outfits]

    # --- Randomly Select Items ---
    selected_outfit = random.choice(outfits)
    selected_shoes = random.choice(shoes)
    selected_accessory = random.choice(accessories)
    nails = [
        "Cat Eye", 
        "French Tip with Cat Decals", 
        "Glitter Ombre with Stars", 
        "3D Flower Nail with Matte Finish", 
        "Ombre", 
        "Matte", 
        "Short with Stickers", 
        "Long with Rhinestones", 
        "Extensions with Tiny Charms"
    ]
    selected_nail = random.choice(nails)

    # --- Style Summary ---
    st.subheader("Style Summary")
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
st.markdown("<p style='text-align:center;'>I just graduated, so this project is not perfect. Please be kind and enjoy my work!</p >", unsafe_allow_html=True)
