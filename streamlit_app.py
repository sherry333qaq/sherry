import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="Style Advisor", layout="wide")

# --- Y2K Pink-Black Background ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff8efb, #000000); /* Pink-Black Gradient */
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title and Author ---
st.title("Style Advisor")
st.markdown("By Sherry | Business: tuxr2021@163.com")

# --- User Information ---
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

# --- Upload Photo ---
st.header("Step 2: Upload Your Photo")
user_file = st.file_uploader("Upload your photo", type=["jpg","png"])
if user_file:
    user_image = Image.open(user_file).convert("RGBA")
    st.image(user_image, caption="Your photo", use_column_width=True)

# --- Generate Recommendations ---
st.header("Step 3: Generate Recommendations")
if st.button("Generate Recommendations"):
    # Outfits
    outfits = [
        {"name":"White Pleated Dress", "price":150},
        {"name":"Red Mini Skirt", "price":120},
        {"name":"Baggy Denim Pants", "price":100},
        {"name":"Crop Top Hoodie", "price":80},
        {"name":"Platform Shoes Outfit", "price":200},
        {"name":"Hanfu", "price":300}
    ]
    filtered_outfits = [o["name"] for o in outfits if o["price"] <= budget]
    selected_outfit = filtered_outfits[0] if filtered_outfits else "No suitable outfit in budget"

    # Shoes
    shoes = [
        {"name":"Platform Sneakers", "price":120},
        {"name":"Chunky Boots", "price":200},
        {"name":"High Heels", "price":250},
        {"name":"HOODIE Flats", "price":100},
        {"name":"Sandals", "price":90}
    ]
    filtered_shoes = [s["name"] for s in shoes if s["price"] <= budget]
    selected_shoes = filtered_shoes[0] if filtered_shoes else "No suitable shoes in budget"

    # Nails
    nails = ["Cat Eye","French Tip","Glitter","3D Decals","Ombre","Matte","Short","Long","Extensions"]
    selected_nail = nails[0]

    # Accessories
    accessories = ["Mini Backpack","Tiny Sunglasses","Choker","Bucket Hat","Earrings","Bracelets","Rings"]
    selected_accessory = accessories[0]

    # Style Summary
    st.subheader("Style Summary")
    st.write(f"Recommended Outfit: **{selected_outfit}**")
    st.write(f"Recommended Shoes: **{selected_shoes}**")
    st.write(f"Recommended Nail Style: **{selected_nail}**")
    st.write(f"Recommended Accessory: **{selected_accessory}**")
    st.write(f"Your preferred colors: {', '.join(favorite_colors) if favorite_colors else 'No preference'}")
    st.write(f"Selected Occasion: {occasion}")
    st.write(f"Your Budget: ${budget}")

# --- Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>I just graduated, so this project is not perfect. Please be kind and enjoy my work!</p >", 
    unsafe_allow_html=True
)
