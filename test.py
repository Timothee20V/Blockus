from PIL import Image

image = Image.open('piece5.png')

# rotate 270 degrees counter-clockwise
imRotate = image.rotate(90)
filename = 'piece5.png'
imRotate.save(filename)

