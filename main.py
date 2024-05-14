import streamlit as st
from PIL import Image
with st.expander("Start camera"):
    camera = st.camera_input("Camera")

uploaded_image = st.file_uploader("Upload Image")
if camera:


    img = Image.open(camera)
    grey_img = img.convert("L")
    st.image(grey_img)
elif uploaded_image:
    img2 = Image.open(uploaded_image)
    grey_img2 = img2.convert("L")
    st.image(grey_img2)