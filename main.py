import cv2
import numpy as np

# Capture video
video_capture = cv2.VideoCapture(0)  # Change to your video source (0 for webcam)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280, 720))  # Adjust resolution if needed

# Read first frame and convert to grayscale
ret, prev_frame = video_capture.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

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
    
    # Filter contours by area
    min_area = 100
    for contour in contours:
        if cv2.contourArea(contour) > min_area:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
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