import cv2
import numpy as np
import OPi.GPIO as GPIO
from time import sleep
import os
#Import all neccessary features to code.


#If code is stopped while the solenoid is active it stays active
#This may produce a warning if the code is restarted and it finds the GPIO Pin, which it defines as non-active in next line, is still active
#from previous time the code was run. This line prevents that warning syntax popping up which if it did would stop the code running.
GPIO.setwarnings(False)
#This means we will refer to the GPIO pins
#by the number directly after the word GPIO. A good Pin Out Resource can be found here https://pinout.xyz/
GPIO.setmode(GPIO.BCM)
#This sets up the GPIO 18 pin as an output pin
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 1)

    
# Capture video
    
video_capture = cv2.VideoCapture(0)  # Change to your video source (0 for webcam)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280, 720))  # Adjust resolution if needed

# Read first frame and convert to grayscale
ret, prev_frame = video_capture.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
photo_directory = "detected_photos"
if not os.path.exists(photo_directory):
    os.makedirs(photo_directory)

movement_detected = False  # Variable to track movement detection
photo_counter = 0
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate absolute difference between current frame and previous frame
    frame_diff = cv2.absdiff(gray, prev_gray)
    
    # Apply thresholding
    _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours by area and detect movement
    min_area = 100
    for contour in contours:
        if cv2.contourArea(contour) > min_area:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            movement_detected = True  # Set movement detected to True
    
    # If movement is detected, run a command in terminal
    if movement_detected:
        # photo_name = os.path.join(photo_directory, f"movement_{photo_counter}.jpg")
        # cv2.imwrite(photo_name, frame)
        # print(f"Movement detected. Photo saved as {photo_name}")
        # photo_counter += 1
        GPIO.output(18, 0)
        sleep(5)
        print("Movement Detected")
        movement_detected = False  # Reset movement detection
    
    # Write the frame to the output video
    out.write(frame)
    
    # Display frame
    cv2.imshow('Fabric Movement Detection', frame)
    
    # Update previous frame
    prev_gray = gray
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture, writer, and close windows
video_capture.release()
out.release()
cv2.destroyAllWindows()
