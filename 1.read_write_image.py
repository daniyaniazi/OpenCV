import cv2


#read image
img=cv2.imread("images/lena.jpg",0)
print(img)

#show iamge
#window name
cv2.imshow("image",img)
#image will dissapear after millisecond

#keyboard binding function
#cv2.waitKey(2000) millisecond
key=cv2.waitKey(0)


if key==27:
    cv2.destroyAllWindows()

elif key==ord("s"):
    cv2.imwrite("images/LENA_copy.png", img)



