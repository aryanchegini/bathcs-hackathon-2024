import serial
import cv2
from time import sleep
arduino = serial.Serial('/dev/cu.usbmodem1301', 9600, timeout=0.1)
cap = cv2.VideoCapture(0)
print("connected to: " + arduino.portstr)
def take_pic():
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
        take_pic()  # Take a picture if the message is 'b'
    
    if msgRD:  # Print the received message if it's not empty
        print(f"Message received from the Arduino: {msgRD}\n")
    #sleep(3)


