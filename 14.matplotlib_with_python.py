import cv2
from matplotlib import pyplot as plt

img = cv2.imread("images/lena.jpg",-1)
cv2.imshow("image",img)
mimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(mimg)
#hide tick value on x and y axis
#plt.xticks([],plt.yticks([]))
plt.show()
#opencv reads image img in bgr format and matplotlib read image in rbg format
#covert image
cv2.waitKey(0)
cv2.destroyAllWindows()