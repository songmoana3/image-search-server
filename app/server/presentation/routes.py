from fastapi import APIRouter

from app.server.presentation import img_search_endpoint
from app.server.infrastructure.DTO import ResultDTO

router_image_search = APIRouter(
    tags=['Image Search']
)

router_image_search.add_api_route(
    path='/image-search',
    endpoint=img_search_endpoint.search_image,
    methods=['POST'],
    response_description='이미지 서치 결과',
    summary='유사 이미지 검색 API',
    response_model= ResultDTO
)