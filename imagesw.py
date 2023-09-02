import streamlit as st
from PIL import Image

# st.write("Image")
image = Image.open('pages/bmc_qr.png')
# print(image)
st.image(image , caption="buy me a coffee")
# image.show()