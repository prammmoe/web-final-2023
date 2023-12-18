import streamlit as st

st.set_page_config(
    page_title="Banana Leaf Disease Classification App",
    page_icon="🍌",
    layout="wide",
    initial_sidebar_state="auto",
)

st.header("About This Project")

col1, col2 = st.columns([3, 1])

with col1:
    st.text("This project goal is to classify banana leaf disease using three neural networks models as mentioned in home section")

with col2:
    st.text("Our goal is to faster early detection of leaf disease in banana before it spreads out.")