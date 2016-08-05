import re

from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from tvil.items import AdItem


class CollectorSpider(CrawlSpider):

    name = 'collector'
    allowed_domains = ['tvil.ru']

    rules = (
        # next page traversal
        Rule(LinkExtractor(restrict_css='li.next')),
        # item extraction
        Rule(
            LinkExtractor(restrict_css='a.Button--openEntity'),
            callback='parse_ad_item'
        ),
    )

    def __init__(self, region='krym', *args, **kwargs):
        super(CollectorSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://tvil.ru/city/%s' % region]

    def parse_ad_item(self, response):

        item = AdItem()

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
                item['ad_id'] = m.group(1)
                item['address'] = m.group(2)

        item['image_urls'] = response.css(
            'img[data-image-big]::attr(data-image-big)'
            ).extract()

        # a = response.css('div.price-start > div > b::text').extract()
        # if a:
        #     item['price'] = a[0]
        item['price'] = ' '.join(
            response.css(
                '''
                div.price-start >
                div.btn-default.btn-block.btn-lightgray.btn-lg
                ::text
                '''
            ).extract()
        ).strip()

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

        a = response.css(
            '.owner > .row > div > h3 > ::text'
            ).extract()
        if a:
            item['owner_name'] = a[0]

        a = response.xpath(
            '//p[starts-with(@id, "description_")]/text()'
            ).extract()
        if a:
            item['description'] = a[0]

        item['misc_info'] = response.css('span.txt::text').extract()

        yield item
