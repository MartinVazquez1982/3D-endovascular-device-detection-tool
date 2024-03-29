import streamlit as st
import time
import subprocess
import os

st.set_page_config(
    page_title="WEB Segmentation",
    page_icon=r'.\\images\\icon.png',
    layout='centered',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

inferenceOk = False
noImage = False

st.title('3D Brain Aneurysm Detection Tool')
st.header('Basic segmentacion model of devices for the treatment of cerebral aneuryms from 3D medical images')
imagen = st.file_uploader("Upload your image below", type=["nii", "gz"])
if imagen is not None:
    source_user_image_path = ".\source_user_image"
    imagen_path = os.path.join(source_user_image_path, "user_image.nii.gz")
    with open(imagen_path, "wb") as f:
        f.write(imagen.read())
left, right = st.columns([10,5])
with left:
    button = st.button('Get segmentation')
    if button and (imagen is not None):
        with st.spinner('Wait for it...'):
            time.sleep(5)
            imagen_path = os.path.abspath(imagen_path)
            subprocess.run(["python", ".\getInference.py", imagen_path])
            inferenceOk = True
    elif button and (imagen is None):
        noImage = True
with right:
    st.text('Segmentation options')
    right_left, right_right = st.columns(2)
    with right_left:
        artery = st.checkbox('Artery', value=True)
    with right_right:
        web = st.checkbox('WEB', value=True)
if inferenceOk:
    st.success('Inferencia obtenida con exito!')
    button = st.button('Download')
if noImage:
    st.error('Image not uploaded')
    

# st.page_link('app.py', label="Home")
# st.page_link(r'.\\pages\\about.py', label="About")

