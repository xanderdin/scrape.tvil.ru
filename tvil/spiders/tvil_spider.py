import scrapy
import re

from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from tvil.items import TvilItem


class TvilSpider(CrawlSpider):
    name = 'krym'
    allowed_domains = ['tvil.ru']
    start_urls = [
        'http://tvil.ru/city/otdyh-v-krymu',
    ]
    rules = (
        Rule(LinkExtractor(restrict_css='li.next')),
        Rule(
            LinkExtractor(restrict_css='a.Button--openEntity'),
            callback='parse_ad_item'
        ),
    )

    def parse_ad_item(self, response):
        item = TvilItem()
        for k in item:
            item[k] = ''
        item['url'] = response.url
        a = response.css(
            '.EntityPage-Main > div.container-fluid > div > h1::text'
            ).extract()
        if a:
            item['title'] = a[0]
        a = response.css(
            '.EntityPage-Main > div.container-fluid > div > p > a::text'
            ).extract()
        if a:
            m = re.search(r'TVIL (\d+-\d+) (.*)', a[0])
            if m:
                item['tvil_id'] = m.group(1)
                item['address'] = m.group(2)

        item['img_urls'] = response.css(
            'img[data-image-big]::attr(data-image-big)'
            ).extract()

        # item['price'] = response.css('.price-start > div').extract()

        a = response.css('.big_number::text').extract()
        if a:
            l = len(a)
            if l >= 1:
                item['nr_floors'] = a[0]
            if l >= 2:
                item['nr_rooms'] = a[1]
            if l >= 3:
                item['nr_guests'] = a[2]
            if l >= 4:
                m = re.search(r'(\d+)', a[3])
                if m:
                    item['square'] = m.group(1)

        # item['nr_floors'], item['nr_rooms'], item['nr_guests'], item['square'] \
        #     = response.css('.big_number::text').extract()

        item['owner_name'] = response.css(
            '.owner > .row > div > h3 > ::text'
            ).extract()

        a = response.xpath(
            '//p[starts-with(@id, "description_")]/text()'
            ).extract()

        if a:
            item['description'] = a[0]

        yield item