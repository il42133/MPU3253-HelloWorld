import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

init_size = 0
init_x = -1
init_y = -1

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        if init_size == 0:
            init_size = w*h
        if init_x < 0 or init_y < 0:
            init_x = x
            init_y = y
        if w*h > init_size*1.2:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        elif x < init_x*0.8 or x > init_x*1.2 or y < init_y*0.8 or y > init_y*1.2:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        else:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #print(init_x, x)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()
