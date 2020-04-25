import cv2

img1= cv2.imread("images/FACE.jpeg")
img2= cv2.imread("images/lena.jpg")

#ADD method
#calculates pre elemts sum of two aarays/scalar
#resize the imahes

img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))

dst=cv2.add(img1,img2)
dst1=cv2.addWeighted(img1,0.6,img2,.4,0)

cv2.imshow("weight",dst1)
cv2.imshow("image",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()