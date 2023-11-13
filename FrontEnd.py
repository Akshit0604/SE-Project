import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load the model
model = tf.keras.models.load_model('air_quality_model.keras')

# Define the image size
img_size = (224, 224)

st.title('Air Quality Index Predictor')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")