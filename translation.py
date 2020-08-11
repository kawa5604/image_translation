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
#cv2.waitKey(0)
