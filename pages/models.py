import streamlit as st

from models.modelManager import ModelManager

st.title('Models Specification')
st.subheader('Basic information of each model')

st.dataframe(ModelManager.getDataFrameMetrics(), hide_index=True, use_container_width=True)

st.info('The data presented for the models may correspond to the best fold, the average of all folds or another specific evaluation method.', icon="ℹ️")