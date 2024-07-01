import streamlit as st
import time
import subprocess
import os
from scripts import getInferenceFront as getInf

def home():
    
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
        source_user_image_path = os.path.join("frontend","source_user_image")
        source_user_inference_path = os.path.join("frontend","source_inference")
        
        # if not exists the directory, it is create
        if not os.path.exists(source_user_image_path):
            os.makedirs(source_user_image_path)
            
        if not os.path.exists(source_user_inference_path):
            os.makedirs(source_user_inference_path)
        
        # It is load the image in the memory
        imagen_path = os.path.join(source_user_image_path, "user_image.nii.gz")
        with open(imagen_path, "wb") as f:
            f.write(imagen.read())


    left, right = st.columns([10,5])

    # Get segmentation button and send the request
    with left:
        button = st.button('Get segmentation')
        if button and (imagen is not None):
            with st.spinner('Wait for it...'):
                time.sleep(5)
                imagen_path = os.path.abspath(imagen_path)
                result = subprocess.run('sbatch /home/mvazquez/frontend/scripts/EXE_runService.sh', shell=True, capture_output=True, text=True)
        
        # Verificar si el subproceso terminó exitosamente
                if result.returncode == 0:  # El código de retorno 0 indica éxito
                    inferenceOk = True
                else:
                    st.error('Error al realizar la inferencia. Consulta los registros para más detalles.')
        elif button and (imagen is None):
            noImage = True

    # Segmentation options
    with right:
        st.text('Segmentation options')
        right_left, right_right = st.columns(2)
        with right_left:
            artery = st.checkbox('Artery', value=True)
        with right_right:
            web = st.checkbox('WEB', value=True)
            
    # Segmentation request result
    if inferenceOk:
        st.success('Inferencia obtenida con exito!')
        button = st.button('Download')
        # if button:
        #     d.downloadResult()

    if noImage:
        st.error('Image not uploaded')


