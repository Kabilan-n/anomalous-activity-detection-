# import the necessary packages
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
#import time
from PIL import Image
from scipy.spatial import distance as dist
#import os
import cv2

import streamlit as st

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)
    print(bytes_data)
