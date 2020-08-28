import scrapy
from ..items import MainPageItem

class EbayItemsSpider(scrapy.Spider):
    name = 'EbayItemsSpider'
    allowed_domains = ['ebay.ca']
    start_urls = [
        "https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=weights&_sacat=0"
        ]

    def parse(self, response):

        mainpage = response.xpath("//*[@class='s-item    ']")

        for item in mainpage:
            itm = MainPageItem()

            itm_title = item.xpath('.//div/div[@class="s-item__info clearfix"]/a/h3/text()').extract_first()
            itm_link = item.xpath('.//div/div[@class="s-item__info clearfix"]/a/@href').extract_first()
            itm_wholeprice = item.xpath('.//div[@class="s-item__info clearfix"]/div[@class="s-item__details clearfix"]/div[@class="s-item__detail s-item__detail--primary"]/span[@class="s-item__price"]/span/text()').extract_first()

            if itm_title and itm_link:
                itm_title = itm_title.strip()
                if itm_title[0] and itm_title[-1] != '\"':
                    itm_title = '\"' + itm_title + '\"'
                
                itm['item_name'] = itm_title
                itm['item_link'] = itm_link.strip()
                if itm_wholeprice:
                    itm['item_price'] = itm_wholeprice.strip()
                yield itm
