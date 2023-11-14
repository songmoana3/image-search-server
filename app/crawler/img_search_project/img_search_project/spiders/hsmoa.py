import re
import scrapy

import img_search_project.settings as st
from img_search_project.items import SongmoanaProjectItem
from img_search_project.utils import get_header, get_hash

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import (DNSLookupError, TCPTimedOutError,
                                    TimeoutError)


class HsmoaSpider(scrapy.Spider):
    name = st.HSMOA
    allowed_domains = ['hsmoa.com']    

    def __init__(self, start_date=None, end_date=None, **kwargs):
        super(HsmoaSpider, self).__init__(**kwargs)
        
        self.headers = get_header()
        self.start_date = int(start_date) # 시작 날짜
        self.end_date = int(end_date)     # 종료 날짜
        self.site = "https://hsmoa.com/" 
        
        self.request_url = f'https://hsmoa.com/?date=[req_date]&site=&cate='
        self.detail_link = 'https://hsmoa.com/i?id=[req_id]&from=web_timeline'

    def start_requests(self): # 메인 상품 리스트 호출
        
        while self.start_date <= self.end_date:
            yield scrapy.Request(
                url=self.request_url.replace('[req_date]', str(self.start_date)),
                headers=self.headers,
                callback=self.parse,
                errback=self.http_error,
                encoding='utf-8',
            )
            
            # 다음 날짜로 이동
            self.start_date += 1


    def parse(self, response): # 썸네일, id 값 추출
        
        if response.status != 200:
            raise HttpError

        if not response.text:
            raise HttpError
        
        product_ls = response.css('.timeline-group') # 전체 상품 목록 추출
        product_ls = product_ls.css('.disblock') # 상품 정보 태그 추출
        
        for product in product_ls: # 상품 정보 - 썸네일 , product_id 추출

            thumbnail = product.css('img.lazy::attr(data-src)').get() # 썸네일 이미지
            hashed_feature =get_hash(thumbnail)

            product_id = product.css('.disblock::attr(href)').get() # product id
            match = re.search(r'id=(\d+)',product.extract()) 
            product_id = str(match.group(1)) if match else None

            hsmoa_item = SongmoanaProjectItem()
            hsmoa_item['hashed_feature'] = hashed_feature
            hsmoa_item['product_id'] = product_id if product_id else None
                
            if product_id:
                yield scrapy.Request(
                    url=self.detail_link.replace('[req_id]', product_id),
                    headers=self.headers,
                    callback=self.detail_parse,
                    errback=self.http_error,
                    encoding='utf-8',
                    meta={'hsmoa_item': hsmoa_item.copy()}
                )
        
    def detail_parse(self, response): # 상세페이지 - 상품명, 가격, 쇼핑몰 추출
        
        hsmoa_item = response.meta['hsmoa_item']
        
        if response.status != 200:
            raise HttpError

        if not response.text:
            raise HttpError
        
        product_name = response.css('.font-24::text').get()
        price = response.css('.font-24.c-red.strong::text').get()
        shopping_mall = response.css('td[style*="color: #222; font-size: 14px; vertical-align: top;  letter-spacing: -1px; line-height:18px;"]::text').get()

        hsmoa_item['product_name'] = product_name if product_name else None
        hsmoa_item['price'] = price.strip() if price else None
        hsmoa_item['shopping_mall'] = shopping_mall.strip() if shopping_mall else None
        hsmoa_item['url'] = response.url
        
        yield hsmoa_item


    # manage error
    def http_error(self, failure):
        self.logger.info(repr(failure))
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.info('HttpError on %s', response.url)
        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.info('DNSLookupError on %s', request.url)
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.info('TimeoutError on %s', request.url)
