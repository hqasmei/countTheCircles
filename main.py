# @Author: hqasmei
# @Date:   2020-10-12T22:19:02-07:00
# @Last modified by:   hosna
# @Last modified time: 2020-10-13T00:04:19-07:00

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_image():
    im = Image.new("RGB", (512, 512), (128, 128, 128))
    draw = ImageDraw.Draw(im)
    draw.ellipse((20, 20, 100, 100), fill = 'black', outline ='black')
    im.save('image.png')

def count_cirles():
    image = cv2.imread('circle_ellipse_2.jpg')
    output = image.copy()
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Find circles
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 200)
    print(circles)
    # If some circle is found
    if circles is not None:
       # Get the (x, y, r) as integers
       circles = np.round(circles[0, :]).astype("int")
       print(circles)
       # loop over the circles
       for (x, y, r) in circles:
          cv2.circle(output, (x, y), r, (0, 255, 0), 2)
    # show the output image
    cv2.imshow("circle",output)
    cv2.waitKey(0)


if __name__ == "__main__":
    create_image()
    count_cirles()
