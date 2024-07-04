import streamlit as st
import time
import datetime
import os

    
inferenceOk = False
noImage = False
inference_script_path = None

# title of the page
st.title('3D Brain Aneurysm Detection Tool')
st.header('Basic segmentacion model of devices for the treatment of cerebral aneuryms from 3D medical images')

# image upload
imagen = st.file_uploader("Upload your image below", type=["nii", "gz"])

if imagen is not None:
    # The image will loaded in the "source_user_image" directory   
    source_user_image_path = os.path.join("source_user_image")
    source_user_inference_path = os.path.join("source_inference")
    
    # if not exists the directory, it is create
    if not os.path.exists(source_user_image_path):
        os.makedirs(source_user_image_path)
        
    if not os.path.exists(source_user_inference_path):
        os.makedirs(source_user_inference_path)
    
    # It is load the image in the memory
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    imagen_path = os.path.join(source_user_image_path, f"image_{timestamp}.nii.gz")
    with open(imagen_path, "wb") as f:
        f.write(imagen.read())


left, right = st.columns([10,5])

# Get segmentation button and send the request
with left:
    button = st.button('Get segmentation')

if button and (imagen is not None):
    with st.spinner('Generating segmentation'):
        time.sleep(10)
        imagen_path = os.path.abspath(imagen_path)
        # Comando

# Verificar si el subproceso terminó exitosamente
        if True:  # El código de retorno 0 indica éxito
            inferenceOk = True
        else:
            st.error(' Error when performing inference', icon='❌')
elif button and (imagen is None):
    noImage = True

# # Select a model
with right:
    option = st.selectbox(
        "Select a model",
        ("Model 0", "Model 1", "Model 2", "Model 5", "Model 10", "Model 11", "Model 15"))
        
# Segmentation request result
if inferenceOk:
    st.success('Inferencia obtenida con exito!')
    button = st.button('Download')
    # if button:
    #     d.downloadResult()

if noImage:
    st.error(' Image not uploaded', icon='❌')


