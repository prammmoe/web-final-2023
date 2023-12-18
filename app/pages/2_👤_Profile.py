import streamlit as st

st.set_page_config(
    page_title="Banana Leaf Disease Classification App",
    page_icon="🍌",
    layout="wide",
    initial_sidebar_state="auto",
)

st.title('Project Goals')
st.text("This project goal is to classify banana leaf disease using three neural networks models as mentioned in home section.")
st.divider()

st.title('Creator')
with st.container():
    col1, col2 = st.columns(2)
    col1.write('')
    col1.write('')
    col1.write('')
    col1.write('**Name:** Pramuditha Muhammad Ikhwan')
    col1.write('**Contact:** ikhwanpramuditha05@gmail.com or [linkedin](https://linkedin.com/in/ikhwanpramuditha)')
    col1.write('Thanks for stopping by!')
    col2.image('./res/image/profile.jpeg', width=360)
st.divider()