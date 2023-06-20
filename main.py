import cv2

source = "image.jpeg"
destination = "newImage3.png"
src = cv2.imread(source)
scale_percent = 10
# cv2.imshow("title", src)

# percentage by which the image is resized


# calculate the 50 percent of original dimension
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (width, height))

cv2.imwrite(destination, output)
cv2.waitKey(0)