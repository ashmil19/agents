# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AgentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()
    job_title = scrapy.Field()
    img_url = scrapy.Field()
    address = scrapy.Field()
    contact_details = scrapy.Field()
    social_accounts = scrapy.Field()
    offices = scrapy.Field()
    languages = scrapy.Field()
    description = scrapy.Field()
