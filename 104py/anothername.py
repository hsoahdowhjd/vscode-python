import cv2
import numpy as np
print("appppppls")
#img = np.array([[[17, 146,  61] , [ 27, 156,  71] , [ 29, 153,  69] , [ 40, 169,  94] , [ 39, 168,  93] , [ 40, 167,  92]], [[ 15, 144,  59] , [ 25, 154,  69] , [ 28, 152,  68] , [ 41, 170,  95] , [ 41, 170,  95] , [ 42, 169,  94]], [[ 13, 142,  57] , [ 23, 152,  67] , [ 27, 151 , 67] , [ 42, 171,  96] , [ 41, 170,  95] , [ 42, 169,  94]]])
black =np.zeros([200,200])
black[20:40,20:180]=127
black[40:190,160:180]=127
#cv2.imread("104-assets/butterfly.jpg")
#print(img)
cv2.imshow("butttttter",black)
cv2.waitKey(0)