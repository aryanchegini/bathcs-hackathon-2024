import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import VGG16
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D, BatchNormalization, Activation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint # type: ignore
import cv2
from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array # type: ignore
from tensorflow.keras.preprocessing.image import load_img # type: ignore
import os
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input # type: ignore
import serial
from time import sleep


model = load_model('github4.h5')
def giveOutput(image_file):
    input_label = {0: 'g', 1: 'c', 2: 'p'}
    img = tf.keras.preprocessing.image.load_img('test_images/bot4.jpg', target_size=(256, 256))
    img_array = tf.keras.preprocessing.image.img_to_array(img) 
    img_array = tf.expand_dims(img_array, 0) 
    predictions = model.predict(img_array)
    output = np.argmax(predictions[0])

    return input_label[output] # This returns g, c, or p


arduino = serial.Serial('COM3', 9600, timeout=0.1)

print("connected to: " + arduino.portstr)
def take_pic():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Capture a single frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        exit()

    # Save the captured image to a file
    cv2.imwrite('captured_image.jpg', frame)

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
    
while True: 
    #msgWR = input("Enter a message to send to the Arduino: ")
    #arduino.write(bytes(msgWR, 'utf-8'))
    msgRD = arduino.readline().decode('utf-8').strip()  # Read and decode the message, strip whitespace
    
    if msgRD == 'b':
        #take_pic()  # Take a picture if the message is 'b'
        letter = giveOutput("captured_image.jpg")
        arduino.write(bytes(letter, 'utf-8'))
        
    
    if msgRD:  # Print the received message if it's not empty
        print(f"Picture taken ")
    #sleep(3)


