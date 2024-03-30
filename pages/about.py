import streamlit as st

def about():
    st.title('About')
    st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eu bibendum metus. Aenean a hendrerit velit, et molestie lorem. Aliquam leo felis, sodales ut euismod sit amet, eleifend a orci. Aenean in nibh vel tortor mollis pulvinar. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi volutpat nisl at velit vulputate sagittis. Sed semper, augue in convallis maximus, mi ligula dapibus nisi, eu dictum mi nibh vestibulum risus. Praesent arcu libero, ullamcorper in tellus non, consequat tempor urna. Nam vulputate ex vitae odio laoreet aliquet. Nulla facilisi. Integer facilisis in ex eu viverra. Interdum et malesuada fames ac ante ipsum primis in faucibus.')
    
    left, centerLeft, x, centerRight,right = st.columns(5)
    
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
        