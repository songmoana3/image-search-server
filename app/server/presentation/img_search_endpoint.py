import logging
from fastapi import HTTPException

from app.server.infrastructure.DTO import QueryImg
from app.server.application_service.img_search_app_service import ImgSearchService


def search_image(
    inbound_data: QueryImg
):
    '''
    유사 이미지 서치 API
    
    Parameters
    
    - **img_url** : 검색 이미지 링크
    '''
    try:
        img_search_service = ImgSearchService(inbound_data)
        img_search_service.preprocess_img()
        result = img_search_service.search_from_es()
        return result
        
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=e.status_code, detail=e.detail)