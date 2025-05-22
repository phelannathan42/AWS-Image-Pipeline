# Example script to test image upload API
import requests

def upload_image():
    url = 'https://your-api-url.amazonaws.com/upload'
    files = {'file': open('example.jpg', 'rb')}
    response = requests.post(url, files=files)
    print(response.text)