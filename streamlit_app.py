import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sherry's AI Style Advisor", layout="wide")
st.title("Sherry's AI Style Advisor")
st.markdown("By Sherry | Business: tuxr2021@163.com")

# --- Step 1: User Information ---
st.sidebar.header("Step 1: Your Info")
face_shape = st.sidebar.selectbox("Face Shape", ["Oval", "Round", "Square", "Heart"])
skin_tone = st.sidebar.selectbox("Skin Tone", ["Cool", "Warm", "Neutral"])
hair_color = st.sidebar.selectbox("Hair Color", ["Black", "Brown", "Blonde", "Other"])
favorite_colors = st.sidebar.multiselect("Favorite Colors", ["Red","Blue","White","Black","Pink","Green"])
preferred_style = st.sidebar.multiselect("Preferred Styles", ["Asian","White Girl","HOODY","Elegant","Casual"])
occasion = st.sidebar.selectbox("Occasion", ["Class","Casual Outing","Date","Party"])

# --- Step 2: Upload Your Photo ---
st.header("Step 2: Upload Your Photo")
user_file = st.file_uploader("Upload your photo", type=["jpg","png"])
if user_file:
    user_image = Image.open(user_file).convert("RGBA")
    st.image(user_image, caption="Your photo", use_column_width=True)

# --- Step 3: Outfit Selection ---
st.header("Step 3: Outfit Selection")
outfits = [
    "White Pleated Dress", "Red Pleated Dress", "Trench Coat", "Long Robe",
    "Avocado Tower Style", "Hanfu"
]
selected_outfit = st.selectbox("Select Outfit", outfits)
st.write(f"Recommended Outfit: **{selected_outfit}** based on your preferences.")

# --- Step 4: Shoes Selection ---
st.header("Step 4: Shoes Selection")
shoes = ["Martens Boots","Heels","HOODY Flat Shoes","Sneakers","Sandals"]
selected_shoes = st.selectbox("Select Shoes", shoes)
st.write(f"Recommended Shoes: **{selected_shoes}**")

# --- Step 5: Nail Selection ---
st.header("Step 5: Nail Selection")
nails = ["Cat Eye","French","Artistic","Plain","Extension","Non-Extension"]
selected_nail = st.selectbox("Select Nail Style", nails)
st.write(f"Recommended Nail Style: **{selected_nail}**")

# --- Step 6: Accessories ---
st.header("Step 6: Accessories")
accessories = ["Sunglasses","Hat","Minimal Jewelry","Bag","Scarf"]
selected_accessory = st.selectbox("Select Accessory", accessories)
st.write(f"Recommended Accessory: **{selected_accessory}**")

# --- Step 7: Hair & Makeup Analysis ---
st.header("Step 7: Hair & Makeup Advice")
st.subheader("Hair Analysis")
st.write("Based on your hair color and skin tone, your hair color looks good!" if hair_color in ["Black","Brown"] else "Consider adjusting your hair color for the best match.")
st.subheader("Eyebrow Recommendation")
st.write("A natural medium-thick eyebrow suits your face." if face_shape in ["Oval","Heart"] else "Consider slightly thicker eyebrows for balance.")
st.subheader("Eyelash Recommendation")
st.write("You can try eyelash extensions for a more striking look!" if "Elegant" in preferred_style else "Natural lashes are fine.")

# --- Step 8: Style & Occasion Summary ---
st.header("Step 8: Style Summary")
st.write(f"Your preferred styles: {', '.join(preferred_style) if preferred_style else 'No preference'}")
st.write(f"Your favorite colors: {', '.join(favorite_colors) if favorite_colors else 'No preference'}")
st.write(f"Recommended outfit for {occasion}: **{selected_outfit}** with **{selected_shoes}** and **{selected_accessory}**, nail style: **{selected_nail}**.")

st.markdown("---")
st.markdown("📌 Note: All images shown are placeholders. Replace them with actual PNG links from your GitHub to visualize outfit, nail, and accessory images.")
