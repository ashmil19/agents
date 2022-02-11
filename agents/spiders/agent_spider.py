import scrapy


class AgentSpiderSpider(scrapy.Spider):
    name = 'agents'
    start_urls = ['http://https://www.bhhsamb.com/agents/']

    def parse(self, response):
        pass
