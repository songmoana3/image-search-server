from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.server.presentation.routes import router_image_search

def get_server():
    
    server = FastAPI(
        description='Image Search Server - songmoana'
    )
    
    server.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    
    server.include_router(router_image_search)

    return server

app = get_server()