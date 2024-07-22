from picamera2 import Picamera2
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# Initialize the camera
camera = Picamera2()
config = camera.create_still_configuration()
camera.configure(config)

# Start the camera and capture an image
camera.start()
camera.capture_file('image.jpg')
camera.stop()
print("Image Saved")

# Open the captured image
image = Image.open('image.jpg')

# Convert image to grayscale
gray_image = image.convert('L')

# Enhance image contrast
contrast_enhancer = ImageEnhance.Contrast(gray_image)
contrast_image = contrast_enhancer.enhance(2)

# Enhance image brightness
brightness_enhancer = ImageEnhance.Brightness(contrast_image)
bright_image = brightness_enhancer.enhance(1.5)

# Resize the image to double the original size
resized_image = bright_image.resize((bright_image.width * 2, bright_image.height * 2), Image.ANTIALIAS)

# Sharpen the image
sharpen_enhancer = ImageEnhance.Sharpness(resized_image)
sharpened_image = sharpen_enhancer.enhance(2)

# Apply adaptive thresholding
threshold_image = sharpened_image.point(lambda p: 255 if p > 128 else 0)

# Apply a slight blur to reduce noise
blurred_image = threshold_image.filter(ImageFilter.MedianFilter(size=3))

# Perform OCR on the preprocessed image with a character whitelist
custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
text = pytesseract.image_to_string(blurred_image, config=custom_config)
print(text)
