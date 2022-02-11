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

    def parse_details(self, response):
        
        name = response.xpath("//h1[@class='body-title']//text()").extract_first()
        job_title = response.xpath("//*[@class='text-left medium-text mobile-text-center']/span[@class='big-text']/text()").extract_first()
        img_url = response.xpath("//*[@class='agent-photo']/@src").extract_first()
        address = ' '.join(response.xpath("//*[@class='text-left medium-text mobile-text-center']/text()").extract()).strip()