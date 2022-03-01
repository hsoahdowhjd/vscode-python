from email.mime import image
from multiprocessing.connection import wait
import os
from turtle import width
import cv2
import time

path = "105assets"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in [ '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
        
        images.append(file_name)
        
print(len(images))
count = len(images)

frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
out = cv2.VideoWriter('sunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)
for i in range(0,count-1):
    print(images[i])
    frame=cv2.imread(images[i])
    out.write(frame)
    fram = cv2.imread(images[i])
    cv2.imshow("frAme",fram)
    cv2.waitKey(10)
    time.sleep(0.0024)
out.release()
print("done")
print(os.getcwd()+"\sunset.mp4")
