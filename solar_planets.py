import cv2
import os



img=cv2.imread("solar-system.jpg")




cv2.putText(img,"Sun",(100,100),cv2.FONT_HERSHEY_COMPLEX,1.5,(171, 79, 132 ))

cv2.putText(img,"Mercury",(100,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(83, 215, 230))

cv2.putText(img,"Venus",(185,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(95, 212, 124))

cv2.putText(img,"Earth",(285,265),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))

cv2.putText(img,"Mars",(380,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(191, 111, 19))

cv2.putText(img,"Jupiter",(500,120),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.putText(img,"Saturn",(690,120),cv2.FONT_HERSHEY_COMPLEX,0.5,(207, 110, 245))

cv2.putText(img,"Uranus",(970,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))

cv2.putText(img,"Neptune",(1100,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(224, 225, 43))

cv2.imshow("output",img)
cv2.imwrite("solar-systenwithname.jpg",img)

cv2.waitKey(0)
