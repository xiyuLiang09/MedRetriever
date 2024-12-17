from PIL import Image

img = Image.open('img/en2.jpg')
rotated = img.rotate(45)

rotated.save('img/rotated.jpg')
