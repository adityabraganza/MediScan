import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='vision_key.json'
from google.cloud import vision
import re

vision_client = vision.ImageAnnotatorClient()
image = vision.Image()

IMAGE_URI = 'https://5.imimg.com/data5/SELLER/Default/2021/1/BN/EI/AB/29490704/paracetamol-tablets-500x500.jpg'

image.source.image_uri = IMAGE_URI

response = vision_client.text_detection(image=image)

text = response.text_annotations[0].description

imeis = re.findall('[0-9]{14,15}', text)    

print(imeis)