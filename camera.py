import cv2
from matplotlib import pyplot as plt

def take_image():
    print ("1")
    cap = cv2.VideoCapture(0)
    print ("2")
    ret, frame = cap.read()
    if ret:
        print(ret)
        #plt.imshow(frame)
        cv2.imwrite("webcamphoto.jpg", frame)
        cap.release()


print ("okay")

take_image()

