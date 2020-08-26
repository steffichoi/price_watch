import scrapy
from ..items import AmazonItem

class AmazonReviewsSpider(scrapy.Spider):
    name = 'AmazonReviewSpider'
    allowed_domains = ['amazon.com']
    myBaseUrl = "https://www.amazon.com/Yes4All-Adjustable-Dumbbell-40-02-lbs/product-reviews/B07235H4JQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls = []
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,121):
        start_urls.append(myBaseUrl+str(i))
 
    # Defining a Scrapy parser
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
 
            star_rating = data.css('.review-rating')
            comments = data.css('.review-text')

            count = 0 
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': (''.join(comments[count].xpath(".//text()").extract()).lstrip().rstrip())
                     }
                count=count+1
