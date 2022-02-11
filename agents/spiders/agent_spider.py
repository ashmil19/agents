import scrapy
from ..items import AgentsItem

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
        
        items = AgentsItem()
        
        name = response.xpath("//h1[@class='body-title']//text()").extract_first()
        job_title = response.xpath("//*[@class='text-left medium-text mobile-text-center']/span[@class='big-text']/text()").extract_first()
        img_url = response.xpath("//*[@class='agent-photo']/@src").extract_first()
        address = ' '.join(response.xpath("//*[@class='text-left medium-text mobile-text-center']/text()").extract()).strip()
        
        contact_details = {
            'Office' : response.xpath("//*[@data-type='Office']/text()").extract_first(),
            'Cell' : response.xpath("//*[@data-type='Agent']/text()").extract_first(),
            'email' : response.xpath("//*[@class='agent_email']/text()").extract_first()
        }
        
        social_accounts = {
            
            'facebook' : response.xpath("//div[@class='agent-social-icons social']/a[@class='fb']/@href").extract_first(),
            'twitter' : response.xpath("//div[@class='agent-social-icons social']/a[@class='tw']/@href").extract_first(),
            'linkedin' : response.xpath("//div[@class='agent-social-icons social']/a[@class='li']/@href").extract_first(),
            'youtube' : response.xpath("//div[@class='agent-social-icons social']/a[@class='yt']/@href").extract_first(),
            'pinterest' : response.xpath("//div[@class='agent-social-icons social']/a[@class='pi']/@href").extract_first(),
            'instagram' : response.xpath("//div[@class='agent-social-icons social']/a[@class='ig']/@href").extract_first()
        }
        
        offices = response.xpath("//div[@id='team_offices']/a/text()").extract()
        languages = response.xpath("//ul[@class='first']/li/text()").extract()
        description =' '.join(response.xpath("//*[@class='col-sm-24']/p/text()").extract())
        
        
        items['name'] = name
        items['job_title'] = job_title
        items['img_url'] = img_url
        items['address'] = address
        items['contact_details'] = contact_details
        items['social_accounts'] = social_accounts
        items['offices'] = offices
        items['languages'] = languages
        items['description'] = description
        
        yield items