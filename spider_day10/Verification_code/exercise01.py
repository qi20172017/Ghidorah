import pytesseract
from PIL import Image

img = Image.open('./yzm4.jpg')
result = pytesseract.image_to_string(img)
print(result)