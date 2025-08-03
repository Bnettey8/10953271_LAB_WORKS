image_path = 'path/to/your/image.jpg'  # Update this with your image path
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('Original Image', image)
cv2.imwrite('original_image.jpg', image)

cv2.imshow('Grayscale Image', gray_image)
cv2.imwrite('grayscale_image.jpg', gray_image)

cv2.imshow('HSV Image', hsv_image)
cv2.imwrite('hsv_image.jpg', hsv_image)

cv2.imshow('LAB Image', lab_image)
cv2.imwrite('lab_image.jpg', lab_image)

plt.figure(figsize=(10, 5))
plt.hist(gray_image.ravel(), bins=25, range=[0, 25], color='gray')
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid()
plt.show()
