import scrapy 
from jumia.items import JumiaItem
from scrapy.http import Request
#from hashlib import sha1

class jumiaSpider(scrapy.Spider):
    
    name = 'jumiaSpider'
    allowed_domains = ['deals.jumia.sn']
    start_urls = ['https://deals.jumia.sn/voitures']

    
    
    def parse_details(self,response):
        item = JumiaItem()
        proprietes = response.css('div.new-attr-style>h3>span::text').extract()
        item['prix'] = response.css('span.price> span::text').extract_first()
        m = response.css('div.new-attr-style>h3>span>a::text').extract()
        item['marque'] = str(m[0])+" "+str(m[1])
        #item['modele'] = m[1]
    
        item['boite_de_vitesse'] = proprietes[0]
        item['type_de_carburant'] = proprietes[1]
        item['annee'] = proprietes[2]
        item['kilometrage'] = proprietes[3]
        
            
        
        #details_vendeur = response.css('div.seller-details')
        #det = details_vendeur.css('dd>span::text').extract()
        #item['date_post'] = details_vendeur.css('dd>time::text').extract_first()
        # if len(det)==2 :
        #     item['localisation'] = det[1]
        #     item['nom_vendeur'] =  det[0]
        # elif len(det)==1:
        #         item['localisation'] = det[0]
        #         item['nom_vendeur'] =response.css('div.user-pic>img::attr(alt)').extract_first()
        # item['commentaires'] = response.css('div.post-text-content > p::text').extract_first()
        
        
        '''listOfImagesUrl =  response.css('div.slide>img::attr(data-src)').extract()
        concat_url = ""
        for imageurl in listOfImagesUrl :
            result_Of_Hash = sha1(imageurl.encode())
            concat_url =concat_url+"|"+result_Of_Hash.hexdigest() 
        
        item['image_url'] = concat_url'''
    

        yield item


    def parse(self, response):
        

        base_url = 'https://deals.jumia.sn'
        cars_urls =  response.css('a.post-link::attr(href)').extract()
        for car_url in cars_urls : 
            url = base_url+car_url

            yield Request(url = url,callback=self.parse_details)
        

        #next_page_url = response.css('li.next>a::attr(href)').extract_first()

        #if(next_page_url) : 
        	#next_page_url = response.urljoin(next_page_url)
        	#yield scrapy.Request(url = next_page_url,callback = self.parse)