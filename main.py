import pytesseract as tess
'''Add your own pytesseract path in line 3'''
tess.pytesseract.tesseract_cmd=r'C:\Users\KIIT\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
from gtts import gTTS


'''Add your own Image Here'''
text=tess.image_to_string(r'D:\Python Session\b1.png')
'''Prints extracted text from image'''
print(text)

text2speech=gTTS(text,lang='en')
text2speech.save('sample.mp3')
