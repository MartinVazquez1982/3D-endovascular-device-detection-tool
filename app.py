import streamlit as st

st.set_page_config(
    page_title="Segmentation",
    page_icon=r'.\\images\\icon.png',
    layout='centered',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Basic segmentacion model of devices for the treatment of cerebral aneuryms')
img = st.file_uploader('Upload imagen')
left, center, right = st.columns([1,2,2])
with center:
    st.text('')
    st.button('Get segmentation')
with right:
    st.text('Segmentation options')
    right_left, right_right = st.columns(2)
    with right_left:
        artery = st.checkbox('Artery', value=True)
    with right_right:
        web = st.checkbox('WEB', value=True)

st.page_link('app.py', label="Home")
st.page_link(r'.\\pages\\about.py', label="About")
