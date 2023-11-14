from fastapi import HTTPException
from elasticsearch import Elasticsearch

from app.config import settings as st

def connect_es_server():
    try:
        es_server = Elasticsearch(f'http://elastic:{st.ELASTIC_PASSWORD}@{st.ELASTIC_HOST}:{st.ELASTIC_PORT}')
        return es_server
    
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail='ES server Connect Error')