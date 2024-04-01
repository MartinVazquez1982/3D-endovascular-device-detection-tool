import streamlit as st
from PIL import Image

def about():
    st.title('About')
    st.write("During the Supervised Professional Practice (SPP) period, a computer vision project in medicine focusing on brain aneurysm segmentation from 3D medical images was undertaken. This experience for Systems Engineers explored the application of artificial intelligence in medicine, enhancing both diagnosis and treatment. The project followed a combined approach, leveraging both in-person and remote work, with fixed schedules and seamless communication with the Yatiris team. A cyclical methodology of training and evaluation was utilized to optimize the segmentation model's performance, employing tools such as PyTorch, SLURM, and Slicer 3D.")
    left, centerLeft, centerRight, right = st.columns(4)
    
    with left:
        st.write('Creators:') 

    with centerLeft:
        st.write('David Burckhardt')
        st.write('Martin Vazquez Arispe')
        
    with centerRight:
        st.write('Directors:')
        
    with right:
        st.write('Dr. Ignacio Larrabide')
        st.write('Dra. Romina Luciana Muñoz')
        


