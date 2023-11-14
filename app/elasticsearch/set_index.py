from elasticsearch import Elasticsearch
import sys
sys.path.append('/songmoana')
from app.config import settings as st


es = Elasticsearch([f'http://elastic:{st.ELASTIC_PASSWORD}@{st.ELASTIC_HOST}:{st.ELASTIC_PORT}'])

# setting & mapping for index
index_name = st.ELASTIC_INDEX

if not es.indices.exists(index=index_name):

  settings ={
    "settings": {
      "analysis": {
        "filter": {
          "my_shingle_filter": {      
            "type": "shingle",
            "min_shingle_size": 5,
            "max_shingle_size": 5,
          },
          "my_minhash_filter": {
            "type": "min_hash",
            "hash_count": 1,          
            "bucket_count": 512,      
            "hash_set_size": 1,       
          }
        },
        "analyzer": {
          "my_analyzer": {
            "tokenizer": "standard",
            "filter": [
              "my_shingle_filter",
              "my_minhash_filter"
            ]
          }
        }
      }
    },
    "mappings": {
      "properties": {
        "hashed_feature": {
            "type": "dense_vector",
            "dims": 256
        },
        "product_id": {"type": "keyword"},
        "product_name": {"type": "keyword"},
        "shopping_mall": {"type": "keyword"},
        "price": {"type": "keyword"},
        "url": {"type": "keyword"}
      }
    }
  }

  es.indices.create(index=index_name, body=settings) # 인덱스 생성
