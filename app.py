import streamlit as st
from PIL import Image

st.set_page_config(page_title="E-Waste Classifier", page_icon="♻️")

st.title("♻️ AI-Powered E-Waste Classification & Recycling Assistant")
st.write("Upload an e-waste image to classify and get recycling guidance.")

EWASTE_INFO = {
    "Mobile Phone": {"hazard": "Lithium Battery, Lead", "recycle": "Remove battery, take to authorized e-waste center."},
    "Laptop": {"hazard": "Battery, Mercury", "recycle": "Wipe data, remove battery, donate or recycle."},
    "Battery": {"hazard": "Highly Toxic", "recycle": "Tape terminals, give to battery recycler ONLY."},
    "Charger / Cable": {"hazard": "Copper, Plastic", "recycle": "Collect cables, take to e-waste bin."},
}

uploaded = st.file_uploader("Upload E-Waste Image", type=["jpg","jpeg","png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded", use_container_width=True)
    choice = st.selectbox("Select type in image:", list(EWASTE_INFO.keys()))
    if st.button("Classify & Get Guide"):
        info = EWASTE_INFO[choice]
        st.success(f"Detected: {choice}")
        st.error(f"⚠️ Hazard: {info['hazard']}")
        st.info(f"♻️ Recycle: {info['recycle']}")
else:
    st.info("👆 Upload old phone / battery image to start.")

st.caption("Built with Streamlit, Pillow | My_project")