import streamlit as st
import os
import importlib

# Load of the Predictor
file_name = os.getenv('FILE_NAME')
class_name = os.getenv('CLASS_NAME')
module_predictor = importlib.import_module(f"predictors.{file_name}")
class_predictor = getattr(module_predictor, class_name)
    
inferenceOk = False
noImage = False
inference_script_path = None

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
    if f'{imagen.file_id}.nii.gz' not in files:
        imagen_path = os.path.join(source_user_image_path, f"{imagen.file_id}.nii.gz")
        with open(imagen_path, "wb") as f:
            f.write(imagen.read())

left, right = st.columns([10,5])

# Get segmentation button and send the request

# Select a model
with right:
    option = st.selectbox(
        "Select a model",
        ("Model 0", "Model 1", "Model 2", "Model 5", "Model 10", "Model 11", "Model 15"))

with left:
    button = st.button('Get segmentation')

if button and (imagen is not None):
    with st.spinner('Generating segmentation'):
        model = os.path.join('/','home', 'mvazquez', 'models', 'model_10')
        img_output = os.path.join('source_inference', imagen.name)
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
        binary_contents = b"example content"
        st.download_button('Download Inference',binary_contents)

if noImage:
    st.error(' Image not uploaded', icon='❌')


