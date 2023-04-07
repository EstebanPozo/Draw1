#https://betterprogramming.pub/creating-algorithmic-art-with-python-edb5c5ea0a87
from PIL import Image, ImageDraw  # pip install pillow for PIL

# Define the canvas size
width = 1500
height = 500
im = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(im)

# Draw a single line
x1, y1 = 10, 20
x2, y2 = 1000, 50
color = (0, 0, 0)  # rgb
draw.line((x1, y1, x2, y2), fill=color)

# Save the image as a PNG
im.save("rectangles.png", "PNG")