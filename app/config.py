import os

class Setting:

    ELASTIC_HOST= os.getenv('ELASTIC_HOST')
    ELASTIC_PORT= os.getenv('ELASTIC_PORT')
    ELASTIC_PASSWORD= os.getenv('ELASTIC_PASSWORD')
    ELASTIC_INDEX= os.getenv('ELASTIC_INDEX')
    
settings = Setting()