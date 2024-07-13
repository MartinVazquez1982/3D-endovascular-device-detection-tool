import streamlit as st
import os
import importlib
from models.modelManager import ModelManager

# Load of the Predictor
file_name = os.getenv('FILE_NAME')
class_name = os.getenv('CLASS_NAME')
module_predictor = importlib.import_module(f"predictors.{file_name}")
class_predictor = getattr(module_predictor, class_name)
    
inferenceOk = False
noImage = False
inference_script_path = None
imagen_path = None

# Title of the page
st.title('3D Endovascular Device Detection Tool')
st.subheader('Basic segmentacion model of devices for the treatment of cerebral aneuryms from 3D medical images')

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
    
    files = os.listdir(source_user_image_path)
    imagen_path = os.path.join(source_user_image_path, f"{imagen.file_id}.nii.gz")
    if f'{imagen.file_id}.nii.gz' not in files:
        with open(imagen_path, "wb") as f:
            f.write(imagen.read())

left, right = st.columns([10,5])

# Get segmentation button and send the request

# Select a model
with right:
    option_model = st.selectbox( "Select a model", ModelManager.get_models())

with left:
    button = st.button('Get segmentation')

if button and (imagen is not None):
    with st.spinner('Generating segmentation'):
        model = ModelManager.path_model(option_model)
        img_output = os.path.join('source_inference', f"{option_model}-{imagen.name}")
        with open('archivo_vacio.txt', 'w') as archivo:
            pass 
        predictor = class_predictor(model)
        result = predictor.predict(imagen_path, img_output)
        if result:
            inferenceOk = True
        else:
            st.error(' Error when performing inference', icon='❌')
elif button and (imagen is None):
    noImage = True
        
# Segmentation request result
if inferenceOk:
    left, right = st.columns([3,1])
    with left:
        st.success(' Inference obtained successfully!', icon="✅")
    with right:
        with open(img_output, "rb") as file:
            inf_result = file.read()
        st.download_button(
            label='Download Inference',
            data=inf_result,
            file_name=os.path.basename(img_output),
            mime='application/x-gzip'
        )

if noImage:
    st.error(' Image not uploaded', icon='❌')


