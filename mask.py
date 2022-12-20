import numpy as np
from PIL import Image
import cv2

def mask(uploaded_file, gray_file):
	# マスク対象画像読み込み
	img = cv2.imread(uploaded_file, cv2.IMREAD_COLOR)

	# マスク画像読み込み
	imgMask = cv2.imread(gray_file, cv2.IMREAD_GRAYSCALE)

	orginal_height = img.shape[0]
	orginal_width = img.shape[1]
	height = imgMask.shape[0]
	width = imgMask.shape[1]
	imgMask = cv2.resize(imgMask , (int(width*orginal_height/1500), int(height*orginal_width/1500)))

	# マスク画像合成
	img[imgMask==0] = [0,0,0]

	# マスク結果画像を保存
	return cv2.imwrite("./processed/mask.jpg", img)