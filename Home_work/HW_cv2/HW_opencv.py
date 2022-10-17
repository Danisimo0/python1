import cv2

img1 = cv2.imread('img2.jpeg', cv2.IMREAD_GRAYSCALE)

thresh = 128
img_binary = cv2.threshold(img1, thresh, 255, cv2.THRESH_BINARY)[1]
scale_percent = 50
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)
img_blur = cv2.blur(img_binary, (10, 10))
new = img_binary + img_blur

cv2.imwrite("new_image.jpeg", new)
