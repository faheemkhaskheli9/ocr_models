import pytesseract
import cv2

image = cv2.imread("sample_images/simple.png")

data = pytesseract.image_to_string(image=image)

print(data)
