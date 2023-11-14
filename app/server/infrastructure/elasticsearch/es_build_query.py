

# 서치 쿼리 (코사인 유사도)
def build_query(query_hash):
    
    query = {
            "query": {
                "function_score": {
                "query": {
                    "match_all": {}
                },
                "functions": [
                    {
                    "script_score": {
                        "script": {
                        "source": "cosineSimilarity(params.queryVector, 'hashed_feature')",
                        "params": {
                            "queryVector": query_hash
                        }
                        }
                    }
                    }
                ],
                }
            }
            }
    
    return query