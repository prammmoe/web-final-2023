# Library
import numpy as np
import cv2
from keras.models import load_model
import tensorflow as tf
import streamlit as st

# Define classes 
CLASS_NAMES = ['Pestalotiopsis', 'Cordana', 'Healthy', 'Sigatoka']

# Define the app title
st.title('Banana Leaf Disease Classification App')

# Upload image
uploaded_file = st.file_uploader('Upload a banana leaf picture', type=['jpg', 'jpeg', 'png'])

# Submit button
submit = st.button('Predict')

# Convert file to OpenCV image 
file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
opencv_image = cv2.imdecode(file_bytes, 1)

# Displaying image
st.image(opencv_image, channels='BGR')

# Resize image if needed
opencv_image = cv2.resize(opencv_image, (224, 224))

# Convert image to 4 dimension
opencv_image.shape = (1, 224, 224, 3)

# Prediction logic
def prediction(model):
    with st.status("Predicting data...", expanded=True) as status:
        pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(pred)]
        st.text('This is a ' + result + ' banana leaf.')
        status.update(label="Prediction complete!", state="complete", expanded=False)

col1, col2, col3 = st.columns(3)

with col1: 
    model = load_model('./model/resnet/banana_resnet50_model_20-epochs.h5')
    st.header("ResNet50 Predictions")
    if submit:
        if uploaded_file is not None:
            prediction(model)

with col2:
    model = load_model('./model/mobilenetv3/banana_mobile_net_v3_model_10_.h5')
    st.header("MobileNetV3 Predictions")
    if submit:
        if uploaded_file is not None:
            prediction(model)
    
with col3: 
    # Load model 
    model = load_model('./model/efficientnet/banana_efficientnetb7_model_10_.h5') 
    st.header("EfficientNetB7 Predictions")
    if submit:
        if uploaded_file is not None:
            prediction(model)