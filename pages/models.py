import streamlit as st
import pandas as pd

st.title('Models Specification')
st.subheader('Basic information of each model')

data = {
    'Model': [ 'Model 1', 'Model 2', 'Model 3' ],
    'Classification Error Rate': [0.01,0.01,0.01],
    'DICE Coefficient': [0.01,0.01,0.01],
    'Sensitivity': [0.01,0.01,0.01],
    'Precision': [0.01,0.01,0.01],
    'F1 Score': [0.01,0.01,0.01],
    'Specificity':[0.01,0.01,0.01],
    'Accuracy':[0.01,0.01,0.01]
}

df = pd.DataFrame(data)
df = df.reset_index(drop=True)
st.dataframe(df, hide_index=True)

st.info('The metric values are the averange of the 5 fold', icon="ℹ️")