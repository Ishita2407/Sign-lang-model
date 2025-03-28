import os
import cv2
import time
import uuid

# Folder where we'll store the images 
IMAGE_PATH = "CollectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']

number_of_images = 10

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)

    #open camera 
    cap = cv2.VideoCapture(0) # 0 for default camera
    print(f"Collecting images for {label}")
    time.sleep(3)

    for imgnum in range(number_of_images):
        ret,frame = cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(3)

        # To break the camera window press q from keyboard
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    cap.release()