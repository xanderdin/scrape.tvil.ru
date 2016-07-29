# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TvilItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    tvil_id = scrapy.Field()
    img_urls = scrapy.Field()
    phone = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    nr_floors = scrapy.Field()
    nr_rooms = scrapy.Field()
    nr_guests = scrapy.Field()
    square = scrapy.Field()
    owner_name = scrapy.Field()
    description = scrapy.Field()
