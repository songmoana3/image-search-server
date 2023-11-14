import logging
import requests
from PIL import Image
from io import BytesIO

# 정상 이미지 확인
def download_image_from_url(img_url):
    
    try:
        response = requests.get(img_url)
        response.raise_for_status() # response chk
        img = Image.open(BytesIO(response.content))
        if img.format != 'JPEG':
            img = img.convert('RGB')

        return img
    
    except (IOError, requests.exceptions.RequestException, Exception) as e:
        logging.error(e)
        raise ValueError("Unnormal Image.") from e
        