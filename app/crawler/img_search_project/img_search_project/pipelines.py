from elasticsearch import Elasticsearch
from scrapy import Item

import img_search_project.settings as st


class ElasticsearchPipeline:
    def __init__(self, server, index):
        self.server = server
        self.index = index
        self.es = Elasticsearch([self.server])

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        server = st.ELASTICSEARCH_SERVERS
        index = st.ELASTICSEARCH_INDEX
        return cls(server, index)

    def process_item(self, item, spider):
        if isinstance(item, Item):
            data = dict(item)
            self.es.index(body=data, index=self.index)
            return item