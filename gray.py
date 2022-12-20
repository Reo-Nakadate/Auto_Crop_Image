import cv2
import numpy as np


def gray(prediction_file):
	src = cv2.imread(prediction_file)

	# 2値化(マスク画像生成)
	src = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
	src = cv2.inRange(src, (0, 10, 0), (255, 255, 255))

	# return src
	return cv2.imwrite('./processed/gray.jpg', src)