import streamlit as st

from pages import home as h, about as ab

if __name__ == '__main__':

    # Page configuration
    st.set_page_config(
        page_title='WEB Segmentation',
        page_icon=r'.\\images\\icon.png',
        layout='centered',
    )
    
    st.markdown(
        """
        <style>
            .stApp {
                height: 100%;
            }
            .st-emotion-cache-1y4p8pa {
                padding-top: 1rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    home, about = st.tabs(['Home', 'About'])
    
    with home:
        h.home()
            
    with about:
        ab.about()
            