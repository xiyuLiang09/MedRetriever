from PIL import Image
import cv2

def thresh_no(img_path, threshold=100):
    img = Image.open(img_path)
    gray_img = img.convert('L')

    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    threshed = gray_img.point(table, '1')
    return threshed


def thresh(img_path, threshold=127):
    img = cv2.imread(img_path, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    

    ret, threshed = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    return threshold


img_path = r'/mnt/d/111aaa/en2.jpg'
save_path = r'/mnt/d/111aaa/en2_threshed.jpg'

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshed = cv2.threshold(gray, 188, 255, cv2.THRESH_BINARY)

cv2.imshow("title", threshed)
cv2.waitKey(0)
cv2.destroyAllWindows()
