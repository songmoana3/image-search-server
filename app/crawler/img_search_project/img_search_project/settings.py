from img_search_project.utils import get_path
import sys
sys.path.append('/songmoana')
from app.config import settings as st

BOT_NAME = "img_search_proejct"

SPIDER_MODULES = ["img_search_proejct.spiders"]
NEWSPIDER_MODULE = "img_search_proejct.spiders"

LOG_FILE='scray.log'
LOG_LEVEL='INFO'

HSMOA = 'hsmoa'

BASE_PATH = get_path(__file__, 2)

ITEM_PIPELINES = {
    'img_search_project.pipelines.ElasticsearchPipeline': 1,
}

# elastic search
ELASTICSEARCH_SERVERS = f'http://elastic:{st.ELASTIC_PASSWORD}@{st.ELASTIC_HOST}:{st.ELASTIC_PORT}'
ELASTICSEARCH_INDEX = st.ELASTIC_INDEX

USER_AGENT = [
    # 맥북+IE
    ('Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; .NET CLR 2.0.50727;'
     ' .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 3.5.30720; rv:11.0) like Gecko'),
    # 맥북+사파리
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) '
     'Version/13.0.5 Safari/605.1.15'),
    # 맥북+파이어폭스
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0'
    ]

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

CONCURRENT_REQUESTS = 1 # 대용량 데이터 크롤링 시 추가!