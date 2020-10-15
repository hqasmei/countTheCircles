# @Author: hqasmei
# @Date:   2020-10-12T22:19:02-07:00
# @Last modified by:   hosna
# @Last modified time: 2020-10-14T22:22:35-07:00

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_image():
    im = Image.new("RGB", (512, 512), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.ellipse((20, 20, 180, 180),fill ='blue',  outline ='black')
    draw.ellipse((140, 140, 180, 180),fill ='blue',  outline ='black')
    im.save('image.png')

def count_cirles():
    image      = cv2.imread('image.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Find circles with HoughCircles
    circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, minDist=150, param1=200, param2=18, minRadius=5)

    # Draw circles
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x,y,r) in circles:
            cv2.circle(image, (x,y), r, (36,255,12), 3)

    # show the output image
    cv2.imshow("image",image)
    cv2.waitKey(0)


if __name__ == "__main__":
    create_image()
    count_cirles()
