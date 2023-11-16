from PIL import Image

#Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
#import joblib
from keras.preprocessing import image
from io import BytesIO
import tensorflow as tf
from tensorflow.keras.applications import resnet50

# Load the model
model = tf.keras.models.load_model('banana_resnet50_model_20-epochs.h5')

# Define the app
st.title('Banana Leaf Disease Classification App')

# Upload the image
uploaded_file = st.file_uploader('Upload a banana leaf picture', type=['jpg', 'jpeg', 'png'])

# Make the prediction
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  image = image.resize((224, 224))
  image_array = tf.keras.preprocessing.image.img_to_array(image)
  image_array = tf.keras.applications.resnet50.preprocess_input(image_array)
  image_array = tf.expand_dims(image_array, axis=0)

  st.image(image, caption='Uploaded image')

  prediction = model.predict(image_array)
  prediction_class = tf.argmax(prediction, axis=1).numpy()[0]
  
  # predicted_classes = resnet50.decode_predictions(prediction_class, top=5)

  if prediction_class == 0:
    st.error('The banana leaf has Cordana black spot disease.')
  elif prediction_class == 1:
    st.success('The banana leaf is healthy.')
  elif prediction_class == 2:
    st.error('The banana leaf has Pestalotiopsis leaf spot disease.')
  elif prediction_class == 3:
    st.error('The banana leaf has Sigatoka leaf spot disease.')
