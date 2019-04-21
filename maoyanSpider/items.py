# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义抓取的字段内容
    movie_photo = scrapy.Field()#图片
    movie_name = scrapy.Field() #电影标题
    star = scrapy.Field() #评分

    ##详情页面信息
    style = scrapy.Field()#电影类型
    region_time = scrapy.Field() #地区/时长
    release_time = scrapy.Field()#上映时间
    box_office = scrapy.Field() #累计票房
    description = scrapy.Field() #剧情介绍
    comment = scrapy.Field() #评论


