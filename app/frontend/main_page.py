from PIL import Image
import requests
import streamlit as st



# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("Alberta/BC license prediction web app")

# displays a file uploader widget
image = st.file_uploader("Choose an image")

if image is not None:
    st.image(image, width=500)
    files = {"file": image.getvalue()}
    pred = requests.post(f"http://localhost:8080/predict", files=files)
    st.text(pred.text)
