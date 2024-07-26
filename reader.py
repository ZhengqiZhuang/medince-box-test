import cv2 as cv

img = cv.imread("图片路径")
img2 = img[100:150,100:150]
mt =  cv.matchTemplate(img,img2,1)
