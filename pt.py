import pytesseract
import cv2
import numpy as np
from PIL import Image

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)


    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

# print(pytesseract.get_languages(config='export TESSDATA_PREFIX=~/traineddata/tessdata_best-4.1.0'))
img = cv2.imread('img/en2.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rotated1 = rotate_bound(img, -45)
rotated2 = cv2.imread('img/rotated.jpg')
a = pytesseract.image_to_data(rotated2, output_type=pytesseract.Output.STRING, config='')
b = pytesseract.image_to_string(rotated1, config='--psm 1')
# c = pytesseract.image_to_osd(rotated2, config='')

# cv2.imshow("rorated", rotated1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(a)
