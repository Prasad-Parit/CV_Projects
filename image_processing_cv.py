import cv2

# Loading the images that shoud be combined
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Ensure the two images have the same dimensions
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Combine the two images horizontally
combined_img = cv2.hconcat([image1, image2])

# Saving the resulting image
cv2.imwrite('combined_img.jpg', combined_image)

# Display the combined image 
cv2.imshow('Combined Image', combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()