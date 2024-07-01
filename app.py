import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title='WEB Segmentation',
    page_icon= os.path.join('.','images','icon.png'),
    layout='centered',
)

st.html(
    """
    <style>
        .stApp {
            height: 100%;
        }
        .st-emotion-cache-1y4p8pa {
            padding-top: 1rem;
        }
    </style>
    """
)

st.logo(os.path.join('.','images','logo.png'))

pg = st.navigation([
    st.Page(os.path.join('pages', 'home.py'), title="Home", icon="🏠"),
    st.Page(os.path.join('pages', 'models.py'), title="Models ", icon="⚙️"),
    st.Page(os.path.join('pages', 'about.py'), title="About ", icon="📄"),
])
pg.run()
        
            