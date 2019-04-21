# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest

from maoyanSpider.items import MaoyanspiderItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']


    def parse(self,response):

        movie = response.xpath("//div[@class='movies-list']//dl[@class='movie-list']//dd")
        print(len(movie))
        for i_item in movie:
            maoyan_item = MaoyanspiderItem()
            #maoyan_item = MaoyanspiderItem()
            maoyan_item['movie_name'] = i_item.xpath(".//div[@class='channel-detail movie-item-title']/a/text()").extract_first()
            maoyan_item['star'] = "".join(i_item.xpath(".//div[@class='channel-detail channel-detail-orange']//i/text()").extract())
            link = i_item.xpath(".//div[@class='channel-detail movie-item-title']/a/@href").extract_first()
            yield scrapy.Request(  # 传入详情页
                url='https://maoyan.com' + link,
                meta={'item': maoyan_item},
                callback=self.parse_detail)
            # 传到pipeline中，进行数据的清洗和存储
            #yield maoyan_item
        #next_link = response.xpath("//div[@class='movies-pager']//ul[@class='list-pager']//li/a/@href").extract()
        cookies = {
            '__mta': '209147181.1555248317563.1555579162182.1555672727698.32',
            '__mta': '209147181.1555248317563.1555574728587.1555579162182.31',
            '_csrf': '13297b35aa507fed95f21398d5a95de0fa9f09b01126f23eac40473367b7473d',
            '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
            '_lxsdk': 'B9DF66D05EB811E9A28869A320D10E6B29AEDBC4BB5342AAAA305BD7F5DD01E4',
            '_lxsdk_cuid': '16a1c05f681c8-0d18f71cfbf049-3a614f0b-14f6b5-16a1c05f681c8',
            '_lxsdk_s': '16a35425136-7fc-f31-0c8%7C%7C13',
            'lt': 'wr675rDnXrfD5F1Q2glWU9N8zLYAAAAAPQgAAE-8gzsKZ1y2Ce99-M7q-EwjrV5ul9Ip2emrFE5ZSQyP7VJ-YPhpZgo2tM98NR4Haw',
            'lt.sig': '0NnNONjoboKuNMo9l4bnNOPJ-u8',
            'uuid': 'B9DF66D05EB811E9A28869A320D10E6B29AEDBC4BB5342AAAA305BD7F5DD01E4',
            'uuid_n_v': 'v1'
        }
        for i in range(1, 60):
            next_link = '&offset=' + str(i * 30)
            # print('刘蒙：',next_link)
            # yield scrapy.Request("https://maoyan.com/films?showType=3" + next_link, callback=self.parse)
            yield scrapy.Request("https://maoyan.com/films?showType=3" + next_link, cookies=cookies, callback=self.parse)

        '''if next_link:
            print('张宁：',next_link)
            next_link = next_link[len(next_link) - 1]
            print("刘蒙：",next_link)
            yield scrapy.Request("https://maoyan.com/films?showType=3" + next_link, callback=self.parse)'''




    #详情页的解析函数
    def parse_detail(self,response):
        maoyan_item = response.meta['item']
        #response.meta(maoyan_item)
        #detail = response.xpath('/html/body/div[3]/div/div[2]')

        res = response.xpath("//div[@class='movie-index-content box']/span/text()").extract()
        res1 = ''.join(res)
        maoyan_item['box_office'] = res1
        maoyan_item['style'] = response.xpath("//div[@class='movie-brief-container']//ul/li[1]/text()").extract()
        maoyan_item['region_time'] = response.xpath("//div[@class='movie-brief-container']//ul/li[2]/text()").extract()
        maoyan_item['release_time'] = response.xpath("//div[@class='movie-brief-container']//ul/li[3]/text()").extract()
        maoyan_item['description'] = response.xpath("//div[@class='mod-content']//span[@class='dra']/text()").extract()
        maoyan_item['comment'] = response.xpath("//div[@class='comment-content']/text()").extract()

        yield maoyan_item

        #maoyan_item['类别']=detail.xpath('./div/ul/li[1]/text()').extract_first()
'''
        def parse(self, response):
            href = response.xpath("//ul[@class='tags-lines']//ul[@class='tags']//li/a/@href").extract()
            print(len(href))
            for i_href in href:
                # print("https://maoyan.com/films" + i_href)
                yield scrapy.Request("https://maoyan.com/films" + i_href, callback=self.parse_first)




    def start_requests(self):
        cookies = {
            '__mta' : '209147181.1555248317563.1555579162182.1555672727698.32',
            '__mta' : '209147181.1555248317563.1555574728587.1555579162182.31',
            '_csrf' : '13297b35aa507fed95f21398d5a95de0fa9f09b01126f23eac40473367b7473d',
            '_lx_utm' : 'utm_source%3DBaidu%26utm_medium%3Dorganic',
            '_lxsdk' : 'B9DF66D05EB811E9A28869A320D10E6B29AEDBC4BB5342AAAA305BD7F5DD01E4',
            '_lxsdk_cuid' : '16a1c05f681c8-0d18f71cfbf049-3a614f0b-14f6b5-16a1c05f681c8',
            '_lxsdk_s' : '16a35425136-7fc-f31-0c8%7C%7C13',
            'lt' : 'wr675rDnXrfD5F1Q2glWU9N8zLYAAAAAPQgAAE-8gzsKZ1y2Ce99-M7q-EwjrV5ul9Ip2emrFE5ZSQyP7VJ-YPhpZgo2tM98NR4Haw',
            'lt.sig' : '0NnNONjoboKuNMo9l4bnNOPJ-u8',
            'uuid' : 'B9DF66D05EB811E9A28869A320D10E6B29AEDBC4BB5342AAAA305BD7F5DD01E4',
            'uuid_n_v' : 'v1'
        }

        #return [FormRequest("https://maoyan.com/films?showType=3", cookies=cookies, callback=self.parse)]
        '''




