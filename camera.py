import cv2
from matplotlib import pyplot as plt
import time

def take_image():
    print ("1")
    cap = cv2.VideoCapture(0)
    print ("2")
    ret, frame = cap.read()
    if ret:
        print(ret)
        #plt.imshow(frame)
        
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
        time.sleep(2)
        cap.set(cv2.CAP_PROP_EXPOSURE, -8.0)
        cv2.imwrite("webcamphoto.jpg", frame)
        cap.release()


print ("okay")

take_image()

