Parser of tvil.ru
=================

A simple Scrapy spider for getting some data from ads at http://tvil.ru.


## Spider name

- **collector**


## Spider args

- **region**  -- Specify city or region. Default: krym. Ex: region=moskva


### Example

Parse data for region 'krym' and save output to data.csv in CSV format.

> scrapy crawl -o data.csv -t csv -a region=krym collector


For other options run:

> scrapy crawl --help


Scrapy docs: http://doc.scrapy.org
