import streamlit as st
import os

# Title of the page
st.title('About')

# About the project
st.write("During the Supervised Professional Practice (SPP) period, a computer vision project in medicine focusing on brain aneurysm segmentation from 3D medical images was undertaken. This experience for Systems Engineers explored the application of artificial intelligence in medicine, enhancing both diagnosis and treatment. The project followed a combined approach, leveraging both in-person and remote work, with fixed schedules and seamless communication with the Yatiris team. A cyclical methodology of training and evaluation was utilized to optimize the segmentation model's performance, employing tools such as PyTorch, SLURM, and Slicer 3D.")

# Creators and directors section
_, creator, _ , _ , directors, _ = st.columns(6)

with creator:
    st.subheader('Creators')
    
with directors:
    st.subheader('Directors')

left, centerLeft, centerRight, right = st.columns(4)

with left:
    st.write('David Burckhardt')

with centerLeft:
    st.write('Martin Vazquez Arispe')
    
with centerRight:
    st.write('Dr. Ignacio Larrabide')
    
with right:
    st.write('Dra. Romina Luciana Muñoz')

st.divider()

# Images of the institures
leftImg, centerleftImg, centerRightImg,rightImg = st.columns(4)

with leftImg:
    st.image(os.path.join('images','unicen.png'), width=100)

with centerleftImg:
    st.image(os.path.join('images','exactas.png'), width=100)
    
with centerRightImg:
    st.image(os.path.join('images','pladema.png'), width=100)
    
with rightImg:
    st.image(os.path.join('images','yatiris.png'), width=100)