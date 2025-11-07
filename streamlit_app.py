import streamlit as st
from PIL import Image
import random

# --- PAGE SETUP ---
st.set_page_config(
    page_title="AI Y2K Stylist", 
    page_icon="💅", 
    layout="wide"
)

# --- CUSTOM CSS (Y2K NEON & GLASS EFFECT) ---
st.markdown("""
<style>
body {
    background: radial-gradient(circle at 10% 20%, #1b003a, #3d0070, #ff00cc);
    color: #ffffff;
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background: transparent;
}
h1,h2,h3 {
    text-align: center;
    color: #ffb6ff;
    text-shadow: 0 0 15px #ff00ff;
}
.navbar {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 10px 20px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.nav-item {
    color: #ffb6ff;
    margin: 0 15px;
    font-weight: bold;
}
.upload-box, .input-box, .recommend-box {
    background-color: rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 25px;
    margin: 20px auto;
    width: 80%;
    text-align: center;
    box-shadow: 0 0 25px rgba(255,0,255,0.4);
}
button {
    background-color: #ff00ff;
    color: #fff;
    padding: 10px 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- NAVBAR & LOGO ---
st.markdown("""
<div class="navbar">
    <div><h2>💅 AI Y2K Stylist</h2></div>
    <div>
        <span class="nav-item">Home</span>
        <span class="nav-item">Upload</span>
        <span class="nav-item">Gallery</span>
        <span class="nav-item">Contact</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- UPLOAD PHOTO ---
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your photo to get custom Y2K style", type=["jpg","jpeg","png"])
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="✨ Your Uploaded Image ✨", use_column_width=True)

    # --- BODY MEASUREMENTS ---
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    st.subheader("Predicted Body Measurements (Editable)")
    height = st.number_input("Height (cm):", min_value=140, max_value=200, value=random.randint(155,175))
    weight = st.number_input("Weight (kg):", min_value=40, max_value=100, value=random.randint(45,65))
    
    # --- USER PREFERENCE ---
    st.subheader("Your Style Preferences")
    color_pref = st.selectbox("Favorite Color:", ["Pink","Blue","Black","White","Purple","Neon Green"])
    budget = st.slider("Budget ($):", 50, 500, 150, step=10)
    style_pref = st.selectbox("Fashion Style:", ["Y2K","Streetwear","Minimalist","Cute","Glam"])
    st.markdown('</div>', unsafe_allow_html=True)

    # --- MOCK RECOMMENDATION LOGIC ---
    st.markdown('<div class="recommend-box">', unsafe_allow_html=True)
    st.subheader("👗 Recommended Outfit & Accessories")

    # Outfit options by style
    outfits = {
        "Y2K": [("Metallic crop top","Holographic skirt","Butterfly choker & mini heart bag"),
                ("Neon holographic jacket","Vinyl pants","Chain belt & glow shoes")],
        "Streetwear": [("Oversize hoodie","Cargo pants","Snapback & sneakers")],
        "Minimalist": [("White silk blouse","Tailored trousers","Simple necklace & loafers")],
        "Cute": [("Ruffled blouse","Pastel pleated skirt","Heart bag & pastel sneakers")],
        "Glam": [("Sequined top","Leather skirt","Gold necklace & high heels")]
    }

    # Filter by budget
    def budget_filter(items, budget):
        if budget < 150:
            return items[:1]
        elif budget < 300:
            return items[:2]
        else:
            return items

    recommended = random.choice(budget_filter(outfits[style_pref], budget))
    st.write(f"Top: {recommended[0]}")
    st.write(f"Bottom: {recommended[1]}")
    st.write(f"Accessories: {recommended[2]}")
    st.write(f"Budget: ${budget}")
    st.write(f"Style: {style_pref}, Favorite Color: {color_pref}, Height: {height}cm, Weight: {weight}kg")

    # --- NAIL STYLE SELECTION ---
    st.subheader("💅 Nail Style Recommendation")
    nail_options = {
        "Y2K":["Chrome Pink","Holographic Silver","Neon Green","Butterfly Nails"],
        "Streetwear":["Matte Black","Graffiti Art","Neon Orange","Skull Accents"],
        "Minimalist":["Nude","French Classic","Soft White","Transparent"],
        "Cute":["Pastel Pink","Rainbow Tips","Heart Accents","Polka Dots"],
        "Glam":["Glitter Red","Gold Foil","Diamonds Effect","Metallic Ombre"]
    }

    selected_nails = st.multiselect("Select your favorite nail styles:", nail_options[style_pref], default=nail_options[style_pref][0])
    st.write("You selected:", ", ".join(selected_nails))

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<p style="text-align:center;">✨ Enjoy your full Y2K fashion experience! ⚡</p >', unsafe_allow_html=True)

else:
    st.markdown('<p style="text-align:center;">Upload your photo above to start your AI fashion journey 💫</p >', unsafe_allow_html=True)
