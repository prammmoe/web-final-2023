# Library
import numpy as np
import cv2
from keras.models import load_model
import tensorflow as tf
import streamlit as st

# Load model 
model = load_model('app/model/banana_resnet50_model_20-epochs.h5')

# Define classes 
CLASS_NAMES = ['Pestalotiopsis', 'Cordana', 'Healthy', 'Sigatoka']

# Define the app title
st.title('Banana Leaf Disease Classification App')

# Upload image
uploaded_file = st.file_uploader('Upload a banana leaf picture', type=['jpg', 'jpeg', 'png'])

# Submit button
submit = st.button('Predict')

# Prediction logic
def prediction():
    # Convert file to OpenCV image 
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        # Displaying image
        st.image(opencv_image, channels='BGR')
        # st.write(opencv_image.shape)

        # Resize image if needed
        opencv_image = cv2.resize(opencv_image, (224, 224))

        # Convert image to 4 dimension
        opencv_image.shape = (1, 224, 224, 3)

        Y_pred = model.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(Y_pred)]
        st.title('This is a ' + result + ' banana leaf.')

if submit:
    if uploaded_file is not None:
          prediction()
