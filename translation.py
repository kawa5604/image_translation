#!/usr/bin/env python3
"""
Image translation is shifting an image along the x and y axis.
This means you can move an image up, down, left, or right.

"""

import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser(description="Requires an image input and will do translations on it")
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)
cv2.waitKey(0)

# Shifting the original image
# The first part is a translation matrix, this will determine how many pixels will shift
# The translation matrix has to be a floating point array [1, 0, tx]
# Were t is the number of pixels the image will shift. + to the left, - to the right
# Same goes for the y axis, its a floating point array [0, 1, ty]
# Were t is the number of pixels the image will shift. + to the left, - to the right

translationMatrix = np.float32([[1, 0, 50], [0, 1, 50]])
shiftedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted image", shiftedImage)
cv2.waitKey(0)
