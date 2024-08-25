import streamlit as st
import cv2
import mediapipe as mp
import math
import statistics
import net_init
import numpy as np


# Load the model
# Assuming app.py contains the necessary functions for processing
from app import start_video_capture

st.title("Sign Language Recognition")
# Display the video capturing component
start_video_capture()
