from pydantic import BaseModel, validator

from app.image_utils.image_downloader import download_image_from_url


class QueryImg(BaseModel):
    img_url: str
    
    @validator('img_url')
    def valid_img_url(cls, v):
        img = download_image_from_url(v)
        return img


class ResultDTO(BaseModel):
    
    product_id: str
    product_name: str
    price: str
    shopping_mall: str
    url: str