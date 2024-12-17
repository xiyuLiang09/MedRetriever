import pytesseract
from PIL import Image

img = Image.open('img/en2.jpg')
rotated1 = img.rotate(45)

a = pytesseract.image_to_data(img, output_type=pytesseract.Output.STRING, config='--psm 1')
b = pytesseract.image_to_string(img, config='--psm 12')

print(b)
