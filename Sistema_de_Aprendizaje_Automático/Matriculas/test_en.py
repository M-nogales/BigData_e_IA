import easyocr
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

#1. Read the image and greyscale
img = cv2.imread('imgs_test/Cars16.png')
plt.imshow(img)
plt.show()
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_image, cmap='gray')
plt.show()

#2. apply filter and find edges for localization
bfilter = cv2.bilateralFilter(gray_image, 11, 17, 17) #filter for noise reduction and edge retention
edged = cv2.Canny(bfilter, 30, 200) #Edge detection
plt.imshow(edged, cmap='gray')
plt.show()

#3. find contours and apply mask
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
print(location)

mask = np.zeros(gray_image.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0,255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.show()

(x,y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropped_image = gray_image[x1:x2+1, y1:y2+1]
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
#4. read text with easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)
result

#5. print the results
text = result[0][-2]
font = cv2.FONT_HERSHEY_SIMPLEX
res = cv2.putText(img, text=text, org=(approx[0][0][0]-170, approx[1][0][1]+80), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()
print(result[0][-2])