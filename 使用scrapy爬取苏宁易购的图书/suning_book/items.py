# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningBookItem(scrapy.Item):
    big_cate = scrapy.Field()
    small_cate = scrapy.Field()
    small_href=scrapy.Field()
    book_href=scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()

    # small_href_id=scrapy.Field()
    # max_page=scrapy.Field()
