
import scrapy


class SongmoanaProjectItem(scrapy.Item):
    
    product_id = scrapy.Field()     # 상품 id
    hashed_feature = scrapy.Field() # 해시화된 feature
    product_name = scrapy.Field()   # 상품명
    shopping_mall = scrapy.Field()  # 쇼핑몰
    price = scrapy.Field()          # 가격
    url = scrapy.Field()            # url
