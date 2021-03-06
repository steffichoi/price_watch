import scrapy
from ..items import MainPageItem

class AmazonItemsSpider(scrapy.Spider):
    name = 'AmazonItemsSpider'
    allowed_domains = ['amazon.ca']
    start_urls = [
        "https://www.amazon.ca/s?k=weights&rh=n%3A2406112011&ref=nb_sb_noss"
        ]

    def parse(self, response):

        mainpage = response.xpath("//*[@class='s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section']")

        for item in mainpage:
            itm = MainPageItem()

            itm_title = item.xpath('.//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a/span/text()').extract_first()
            itm_link = item.xpath('.//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]/a/@href').extract_first()
            itm_wholeprice = item.xpath('.//span[@class="a-price"]/span/text()').extract_first()

            if itm_title and itm_link:
                itm_title = itm_title.strip()
                if itm_title[0] and itm_title[-1] != '\"':
                    itm_title = '\"' + itm_title + '\"'
                itm['item_name'] = itm_title
                itm['item_link'] = itm_link.strip()
                if itm_wholeprice:
                    itm['item_price'] = itm_wholeprice.strip()
                yield itm
