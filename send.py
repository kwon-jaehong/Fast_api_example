import base64
import requests

url = 'http://localhost:32220/'
with open("image.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    
# payload ={"filename": "photo.png"}

payload ={"filename": "photo.png", "filedata": encoded_string}

resp = requests.post(url=url, data=payload) 