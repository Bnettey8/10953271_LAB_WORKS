original_image = Image.open('photo.jpg')
gray_image = original_image.convert('L')
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)

plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)

plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

gray_image.save('photo_gray.jpg')
