# songmoana-image-search project
> Developer : songmoana  
> Last modified : 23.11.08  
> Contact : songmoana3@gmail.com

## _Update Note_  
- 23-11-08 : Release
    

## _Files required for execution_
-  `.env`


## _Structure_
```
.
├── Dockerfile
├── README.md
├── app
│   ├── config.py
│   ├── crawler
│   │   ├── img_search_project
│   │   │   ├── img_search_project
│   │   │   │   ├── __init__.py
│   │   │   │   ├── items.py
│   │   │   │   ├── middlewares.py
│   │   │   │   ├── pipelines.py
│   │   │   │   ├── settings.py
│   │   │   │   ├── spiders
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── hsmoa.py
│   │   │   │   └── utils.py
│   │   │   └── scrapy.cfg
│   │   └── scrapy_run.py
│   ├── elasticsearch
│   │   ├── _state
│   │   ├── config
│   │   │   └── elasticsearch.yml
│   │   ├── indices
│   │   ├── node.lock
│   │   ├── nodes
│   │   ├── set_index.py
│   │   └── snapshot_cache
│   ├── image_utils
│   │   ├── feature_extractor.py
│   │   ├── hashing.py
│   │   └── image_downloader.py
│   ├── main.py
│   └── server
│       ├── application_service
│       │   └── img_search_app_service.py
│       ├── infrastructure
│       │   ├── DTO.py
│       │   └── elasticsearch
│       │       ├── es_build_query.py
│       │       ├── es_connect.py
│       │       └── es_repository.py
│       └── presentation
│           ├── img_search_endpoint.py
│           └── routes.py
├── docker-compose.yml
└── requirements.txt
```

## _Main Process_  
* Scrapy
    1. `https://hsmoa.com/` 사이트의 상품 데이터를 크롤링합니다.
    2. 크롤링한 데이터를 해시 처리 후 ES에 인덱싱합니다.


## _How to execute_
* Docker  
    1. docker-compose up 으로 실행 
---

* Scrapy 
    1. songmoana-image-search-server 컨테이너 내부에 접속합니다.
    2. `/songmoana/elasticsearch` 경로에서 `python3 set_index.py` 명령어로 ES 인덱스 세팅을 수행합니다.
    3. `/songmoana/crawler` 경로에서 `python3 scrapy_run.py` 명령어로 코드를 실행, 크롤링 날짜를 입력 후 데이터 크롤링을 수행합니다.
---
* Image-Search-API  
    1. http://localhost:3001/docs 에 접속합니다.
    2. request_body 의 img_url 에 이미지 주소를 입력하고 요청합니다.
        * 참고 : 첫 요청 시 model download 받는 시간이 걸립니다.
        * 예시 이미지 링크 : http://thum.buzzni.com/unsafe/320x320/center/smart/http://cdn.image.buzzni.com/2023/08/16/FB9AmHz3.jpg
                            http://thum.buzzni.com/unsafe/320x320/center/smart/http://cdn.image.buzzni.com/2023/09/13/JWS3AiE6.jpg

## _Prerequisite_
1. Linux ubuntu (20.04 recommended)  
2. Docker  
3. python 3.8+ 
4. docker-compose 1.25.0+
5. 32GB RAM+

