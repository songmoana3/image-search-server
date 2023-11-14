
# ES methods
class ElasticSearchRepositoryImpl:
    
    def __init__(self, es, query):
        self.es = es
        self.query = query
        
    def search(self):
        return self.es.search(index='hsmoa', body=self.query)

