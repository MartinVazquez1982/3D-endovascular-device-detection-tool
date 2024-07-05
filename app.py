import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Page configuration
st.set_page_config(
    page_title='WEB Segmentation',
    page_icon= os.path.join('.','images','icon.png'),
    layout='centered',
    initial_sidebar_state="collapsed"
)


st.html(
    """
    <style>
    .block-container {
        padding-top: 55px;
        padding-left: 0px;
        padding-right: 0px;
        padding-bottom: 0px;
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
        
            