import streamlit as st

def about():
    st.title('About')
    st.write("During the Supervised Professional Practice (SPP) period, a computer vision project in medicine focusing on brain aneurysm segmentation from 3D medical images was undertaken. This experience for Systems Engineers explored the application of artificial intelligence in medicine, enhancing both diagnosis and treatment. The project followed a combined approach, leveraging both in-person and remote work, with fixed schedules and seamless communication with the Yatiris team. A cyclical methodology of training and evaluation was utilized to optimize the segmentation model's performance, employing tools such as PyTorch, SLURM, and Slicer 3D.")
    
    leftTitle, rightTitle = st.columns(2)
    
    with leftTitle:
        st.write('Creators:')
        
    with rightTitle:
        st.write('Directors:')
    
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
    
    leftImg, centerleftImg, centerRightImg,rightImg = st.columns(4)
    
    with leftImg:
        st.image(r'images\\unicen.png', width=100)
    
    with centerleftImg:
        st.image(r'images\\exactas.png', width=100)
        
    with centerRightImg:
        st.image(r'images\\pladema.png', width=100)
        
    with rightImg:
        st.image(r'images\\yatiris.png', width=100)