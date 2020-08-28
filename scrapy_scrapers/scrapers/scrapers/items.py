# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MainPageItem(scrapy.Item):
    item_name = scrapy.Field()
    item_link = scrapy.Field()
    item_price = scrapy.Field()

class AmazonItem(scrapy.Item):
    product_name = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_category = scrapy.Field()
    product_original_price = scrapy.Field()
    product_availability = scrapy.Field()


