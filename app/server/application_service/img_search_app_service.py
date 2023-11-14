from app.image_utils.hashing import LSHHash
from app.image_utils.feature_extractor import FeatureExtractor

from app.server.infrastructure.elasticsearch.es_build_query import build_query
from app.server.infrastructure.elasticsearch.es_connect import connect_es_server
from app.server.infrastructure.elasticsearch.es_repository import ElasticSearchRepositoryImpl


class ImgSearchService:
    
    def __init__(self,inbound_data):
        self.inbound_data = inbound_data
    
    def preprocess_img(self):
        feature_extractor = FeatureExtractor(self.inbound_data.img_url) # extract_feature
        feature = feature_extractor.extract_feature()
        
        lsh_hash = LSHHash(256)
        self.hashed_feature = lsh_hash.hash_tensor(feature) # get_hashed_feature
        return self.hashed_feature
    
    def search_from_es(self):
        es_server = connect_es_server() # connect_to_es
        query = build_query(self.hashed_feature) # build_search_query
        
        es_repository_impl = ElasticSearchRepositoryImpl(es_server, query)
        result = es_repository_impl.search()
        
        hits = result['hits']['hits'] # get result
        source = hits[0]['_source'] # get product_info
        return source
