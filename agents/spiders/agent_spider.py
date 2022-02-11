import scrapy


class AgentSpiderSpider(scrapy.Spider):
    name = 'agents'
    start_urls = [
        'http://https://www.bhhsamb.com/agents/'
        ]

    def parse(self, response):
        
        profile_link = response.xpath("//span[@class='agent-name']/a/@href").extract()
        
        for link in profile_link:
            yield response.follow(link, callback=self.parse_details)
