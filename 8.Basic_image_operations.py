import cv2

img= cv2.imread("images/FACE.jpeg")

print(img.shape)#tuple od no of rows ,cols,channels
print(img.size)#return total no of pixels is accessed
print(img.dtype)#return image datatype
b,g,r=cv2.split(img)
img= cv2.merge((b,g,r))
cv2.imshow("image",img)


#roi= region of interest
#area of an image you want to work with
area=img[123:240, 188:280]
print(area.shape)
img[5:122, 302:394]=area
# img[200:317, 200:292]=area
# img[:117, :92]=area
# paste=img[200:317, 200:292]
#dimesions should be excact
paste=img[5:122, 302:394]
print(paste.shape)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


