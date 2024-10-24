import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image
from io import BytesIO

def stitch_images(images):
    opencv_images = [cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR) for img in images]
    stitcher = cv.Stitcher.create()
    (status, stitched) = stitcher.stitch(opencv_images)
    return stitched if status == cv.Stitcher_OK else None

def convert_to_pil(image):
    return Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))

st.set_page_config(layout="wide")
st.title("PanoGen")

with st.sidebar:
    st.header("Upload Images")
    uploaded_files = st.file_uploader("Upload multiple images", accept_multiple_files=True, type=['jpg', 'png', 'jpeg'])

    if uploaded_files:
        images = [Image.open(file) for file in uploaded_files]
        st.write(f"Uploaded {len(images)} images.")
        st.image(images, caption=[f"Image {i + 1}" for i in range(len(images))], width=150)

if uploaded_files:
    if st.button("Generate Panorama"):
        with st.spinner("Generating..."):
            panorama = stitch_images(images)
            if panorama is not None:
                panorama_rgb = cv.cvtColor(panorama, cv.COLOR_BGR2RGB)
                st.image(panorama_rgb, caption="Generated Panorama", use_column_width=True)

                # convert stitched image to PIL format for download
                panorama_pil = convert_to_pil(panorama)
                buf = BytesIO()
                panorama_pil.save(buf, format="JPEG")
                byte_im_panorama = buf.getvalue()

                st.download_button(
                    label="Download Panorama",
                    data=byte_im_panorama,
                    file_name="panorama.jpg",
                    mime="image/jpeg"
                )
            else:
                st.error("Failed to stitch images. Please try again.")
