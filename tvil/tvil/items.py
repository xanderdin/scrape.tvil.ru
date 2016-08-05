# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class AdItem(Item):
    url = Field()
    ad_id = Field()
    image_urls = Field()
    phone = Field()
    title = Field()
    address = Field()
    price = Field()
    nr_floors = Field()
    nr_rooms = Field()
    nr_guests = Field()
    square = Field()
    owner_name = Field()
    description = Field()
    misc_info = Field()
