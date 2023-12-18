# Library
import streamlit as st

st.set_page_config(
    page_title="Banana Leaf Disease Classification App",
    page_icon="🍌",
    layout="wide",
    initial_sidebar_state="auto",
)

# Define the app title
col1, col2 = st.columns([3, 2])

with col1:
    st.title('Welcome to LeafDoc')
    st.write('_Banana Edition_')
    st.subheader('A tool to classify disease in banana leaves.')
    st.divider() 
    st.header('How to use')
    st.markdown(
        """
        1. Go into **Classification** section
        2. Upload a banana leaf picture
        3. Click predict
        4. Wait for your results to came up
        """
    )

    st.write('')
    st.write('')
    st.warning('**Caution**: Make sure you uploaded a banana leaf picture or the models will not running')

with col2: 
    st.image("./res/image/home_illustration.png")

st.text('PS: You can also choose the models that you want to try!')
