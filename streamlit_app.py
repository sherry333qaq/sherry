import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sherry's Y2K Style Advisor", layout="wide")

# --- Y2K Background ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.ibb.co/Y2K-Background.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Sherry's Y2K Style Advisor")
st.markdown("By Sherry | Business: tuxr2021@163.com")

# --- Step 1: User Information ---
st.sidebar.header("Step 1: Your Info")
face_shape = st.sidebar.selectbox("Face Shape", ["Oval","Round","Square","Heart","Diamond","Triangle","Long","Wide"])
skin_tone = st.sidebar.selectbox("Skin Tone", ["Cool","Warm","Neutral","Olive","Pale","Tan","Dark"])
hair_color = st.sidebar.selectbox("Hair Color", ["Black","Dark Brown","Light Brown","Blonde","Red","Pink","Blue","Silver","Ombre"])
eyebrow_type = st.sidebar.selectbox("Eyebrow Type", ["Straight","Arched","Thick","Thin","Natural","Angled"])
eyelash_preference = st.sidebar.selectbox("Eyelash Preference", ["None","Natural","Extensions","Volume","Curl"])
favorite_colors = st.sidebar.multiselect("Favorite Colors", ["Red","Blue","White","Black","Pink","Green","Purple","Yellow","Orange","Silver","Gold","Neon"])
preferred_style = st.sidebar.multiselect("Preferred Styles", ["Y2K","Asian","White Girl","HOODIE","Elegant","Casual","Streetwear","K-Pop","Indie","Girly","Grunge","Minimalist","Cute","Soft","Bold"])
occasion = st.sidebar.selectbox("Occasion", ["Class","Casual Outing","Date","Party","Work","Travel","Clubbing","Festival","Photoshoot"])
budget = st.sidebar.number_input("Your Budget ($)", min_value=50, max_value=10000, step=50, value=200)

# --- Step 2: Upload Photo ---
st.header("Step 2: Upload Your Photo")
user_file = st.file_uploader("Upload your photo", type=["jpg","png"])
if user_file:
    user_image = Image.open(user_file).convert("RGBA")
    st.image(user_image, caption="Your photo", use_column_width=True)

# --- Step 3: Generate Recommendations ---
st.header("Step 3: Generate Your Y2K Recommendations")
if st.button("Generate My Style"):
    # --- Outfits ---
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

    # --- Shoes ---
    shoes = [
        {"name":"Platform Sneakers", "price":120},
        {"name":"Chunky Boots", "price":200},
        {"name":"High Heels", "price":250},
        {"name":"HOODIE Flats", "price":100},
        {"name":"Sandals", "price":90}
    ]
    filtered_shoes = [s["name"] for s in shoes if s["price"] <= budget]
    selected_shoes = filtered_shoes[0] if filtered_shoes else "No suitable shoes in budget"

    # --- Nails ---
    nails = ["Cat Eye","French Tip","Glitter","3D Decals","Ombre","Matte","Short","Long","Extensions"]
    selected_nail = nails[0]

    # --- Accessories ---
    accessories = ["Mini Backpack","Tiny Sunglasses","Choker","Bucket Hat","Earrings","Bracelets","Rings"]
    selected_accessory = accessories[0]

    # --- Hair / Eyebrow / Eyelash Advice ---
    hair_advice = "Your hair color looks trendy for Y2K style!" if hair_color in ["Blonde","Brown","Light Brown"] else "Consider soft highlights for Y2K effect."
    eyebrow_advice = "Thin arched brows suit Y2K style."
    eyelash_advice = "Optional eyelash extensions enhance Y2K vibe."

    # --- Style Summary ---
    st.subheader("Y2K Style Summary")
    st.write(f"Recommended Outfit: **{selected_outfit}**")
    st.write(f"Recommended Shoes: **{selected_shoes}**")
    st.write(f"Recommended Nail Style: **{selected_nail}**")
    st.write(f"Recommended Accessory: **{selected_accessory}**")
    st.write(f"Hair Advice: {hair_advice}")
    st.write(f"Eyebrow Advice: {eyebrow_advice}")
    st.write(f"Eyelash Advice: {eyelash_advice}")
    st.write(f"Your preferred colors: {', '.join(favorite_colors) if favorite_colors else 'No preference'}")
    st.write(f"Selected Occasion: {occasion}")
    st.write(f"Your Budget: ${budget}")

# --- Step 4: Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center;'>I just graduated, so this project is not perfect. Please be kind and enjoy my work!</p >", unsafe_allow_html=True)
