# Library
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Banana Leaf Disease Classification App",
    page_icon="🍌",
    layout="wide",
    initial_sidebar_state="auto",
)

# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2

# Define the app title
col1, col2 = st.columns(2)

with col1: 
    st.title('Banana Leaf Disease Classification App')

with col2:
    st.image("./res/image/download.jpeg")
