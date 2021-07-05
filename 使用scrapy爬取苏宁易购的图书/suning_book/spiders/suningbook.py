import scrapy
from ..items import SuningBookItem
from copy import deepcopy
import re

class SuningbookSpider(scrapy.Spider):
    name = 'suningbook'
    allowed_domains = ['list.suning.com','product.suning.com',r'/*.suning.com']
    start_urls = ['https://book.suning.com/']

    #构造进入小分类的请求
    def parse(self, response):
        items=SuningBookItem()
        big_div_list=response.xpath('//div[@class="menu-list"]/div')
        for div in big_div_list:
            items['big_cate']=div.xpath('./dl/dt/h3/a/text()').extract_first()
            small_cate_list=div.xpath('./dl/dd/a')
            for dd in small_cate_list:
                items['small_cate']=dd.xpath('./text()').extract_first()
                items['small_href']=dd.xpath('./@href').extract_first()
                #items['small_href_id']=dd.xpath('./@name').extract_first().split('_')[2:3][0]
                #进入小分类的上半页
                yield scrapy.Request(
                    url=items['small_href'],
                    callback=self.parse_small_cate,
                    meta={'item':deepcopy(items)}
                )


    #进入小分类，获取店铺标题和图书的部分信息
    def parse_small_cate(self,response):
        items=response.meta['item']
        li_list=response.xpath('//ul[@class="clearfix"]/li')

        for li in li_list:
            items['title']=li.xpath('./div/div/div/div[2]/p[2]/a/text()').extract_first()
            items['book_href']=r'https:'+str(li.xpath('./div/div/div/div[2]/p[2]/a/@href').extract_first())

        #进入图书的详情页面
            yield scrapy.Request(
                items['book_href'],
                callback=self.parser_detail,
                meta={'item':deepcopy(items)}
            )
            #进行翻页
        next_page=response.xpath('//*[@id="nextPage"]/@href').extract_first()
        if next_page!='':
            url=response.urljoin(next_page)
            yield scrapy.Request(
                url=url,
                callback=self.parse_small_cate,
                meta={'item': deepcopy(items)}
            )


    #进入图书详情页面，获取图书的详细信息
    def parser_detail(self,response):
        items=response.meta['item']
        items['author']=response.xpath('//*[@id="proinfoMain"]/ul/li[1]/text()').extract_first()
        yield items
















