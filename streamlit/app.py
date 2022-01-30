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
# tfile.write(f.read())
import streamlit as st
import time
import cv2

if st.button('Start'):
    video = cv2.VideoCapture('https://www.mediacollege.com/video-gallery/testclips/20051210-w50s.flv')
    #video.set(cv2.CAP_PROP_FPS, 25)

    image_placeholder = st.empty()

    while True:
        success, image = video.read()
        if not success:
            break
        image_placeholder.image(image, channels="BGR")
        time.sleep(0.01)

vf = cv.VideoCapture(tfile.name)

# stframe = st.empty()
# outframe = []
# while vf.isOpened():
#     ret, frame = vf.read()
#     # if frame is read correctly ret is True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     outframe.append(gray)
# st.video(outframe)
    #stframe.image(gray)
    
