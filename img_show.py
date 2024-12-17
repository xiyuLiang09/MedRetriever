import cv2
from PIL import Image

prior = cv2.imread('img/en3.jpg')
after = cv2.cvtColor(prior, cv2.COLOR_BGR2GRAY)

cv2.imshow("prior", prior)
cv2.imshow("after", after)

cv2.waitKey(0)
cv2.destroyAllWindows()