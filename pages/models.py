import streamlit as st
import pandas as pd

st.title('Models Specification')
st.subheader('Basic information of each model')

pd.options.display.float_format = '{:.10f}'.format

data = {
    'Model': [ 'Model 0', 'Model 1', 'Model 2', 'Model 5', 'Model 10', 'Model 11', 'Model 15' ],
    'Classification Error': [
        8.5295e-05,
        9.483286e-05,
        0.0003200,
        0.0004929,
        7.9153e-05,
        8.074e-05,
        0.0007504
    ],
    'DICE': [
        0.715142,
        0.7167220,
        0.3912443,
        0.0381241,
        0.7805647,
        0.7869420,
        0.8630332
    ],
    'Sensitivity': [
        0.6398984,
        0.6979077,
        0.2588244,
        0.0245836,
        0.7279169,
        0.7365124,
        0.8424650
    ],
    'Precision': [
        0.8425535,
        0.7996776,
        0.8011073,
        0.0848699,
        0.9003842,
        0.8992160,
        0.8886734
    ],
    'F1 Score': [
        0.715142,
        0.716722,
        0.391244,
        0.0381241,
        0.7805647,
        0.7869420,
        0.8630332
    ],
    'Specificity':[
        0.9999145,
        0.9999718,
        0.9999744,
        0.999894,
        0.9999883,
        0.9999875,
        0.9995986
    ],
    'Accuracy':[
        0.9999147,
        0.9999051,
        0.9996799,
        0.999507,
        0.9999208,
        0.9999192,
        0.9992495
    ]
}

df = pd.DataFrame(data)
df = df.style.format({
    'CER': '{:.7f}',
    'DICE Coefficient': '{:.7f}',
    'Sensitivity': '{:.7f}',
    'Precision': '{:.7f}',
    'F1 Score': '{:.7f}',
    'Specificity':'{:.7f}',
    'Accuracy':'{:.7f}'
})
st.dataframe(df, hide_index=True, use_container_width=True)

st.info('The metric values are the averange of the 5 fold', icon="ℹ️")