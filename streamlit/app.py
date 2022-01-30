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
import cv2 as cv
import tempfile

f = st.file_uploader("Upload file")

tfile = tempfile.NamedTemporaryFile(delete=False) 
tfile.write(f.read())


vf = cv.VideoCapture(tfile.name)

stframe = st.empty()

while vf.isOpened():
    ret, frame = vf.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    stframe.image(gray)
    
