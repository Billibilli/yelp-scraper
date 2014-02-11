import sys
from scrapy.spider import Spider
from scrapy.selector import Selector

from yelpspider.items import YelpspiderItem

class YelpSpider(Spider):
	name = "yelp"
	allowed_domains = ["yelp.com"]
    	start_urls = ["http://www.yelp.com/search?find_desc=&find_loc=Urbana-Champaign%2C+IL&start=1"]
	for i in range(1,100):
        	start_urls.append("http://www.yelp.com/search?find_desc=&find_loc=Urbana-Champaign%2C+IL&start="+str(i*10))

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//*[@id="super-container"]/div[3]/div[3]/div[1]/div/div[1]/ul/li')
		items = []

		for site in sites:
			item = YelpspiderItem()
			name=site.xpath('div/div[1]/div[2]/h3/span/a/text()').extract()
			if len(name)>0:
				item['name'] = name[0]
			else:
				item['name'] = ''

			url=site.xpath('div/div[1]/div[2]/h3/span/a/@href').extract()
			if len(url)>0:
				item['url'] = u'http://www.yelp.com'+url[0]
			else:
				item['url'] = ''

			address_l1=site.xpath('div/div[2]/address/text()[1]').extract()
			if len(address_l1)>0:
				item['address_l1'] = address_l1[0].replace('\n','').strip()
			else:
				item['address_l1'] = ''

			address_l2=site.xpath('div/div[2]/address/text()[2]').extract()
	                if len(address_l2)>0:
	                	item['address_l2'] = address_l2[0].replace('\n','').strip()	
			else:
				item['address_l2'] = ''

			phone=site.xpath('div/div[2]/span[2]/text()').extract()
			if len(phone)>0:
				item['phone']=phone[0].replace('\n','').strip()
			else:
				phone = ''

			item['category'] = site.xpath('div/div[1]/div[2]/div[2]/span[2]/a/text()').extract()

			rating=site.xpath('div/div[1]/div[2]/div[1]/div/i/@title').extract()
			if len(rating)>0:
				item['rating'] = rating[0].split(' ')[0]
			else:
				item['rating'] = ''

			price_rating=site.xpath('div/div[1]/div[2]/div[2]/span[1]/span/text()').extract()
			if len(price_rating)>0:
				item['price_rating'] = unicode(str(len(price_rating[0]))) 
			else:
				item['price_rating'] = ''

			thumbUrl = site.xpath('div/div[1]/div[1]/div/a/img/@src').extract()
			if len(thumbUrl) > 0:
				item['thumbUrl'] = u'http:'+thumbUrl[0]
			else:
				item['thumbUrl'] = ''

			fav_comment_user = site.xpath('div/div[3]/div[1]/div/a/img/@alt').extract()
			if len(fav_comment_user)>0:
				item['fav_comment_user']=fav_comment_user[0] 
			else:
				item['fav_comment_user']=''

			fav_comment_content = site.xpath('div/div[3]/div[2]/p/text()').extract()
			if len(fav_comment_content)>0:
				item['fav_comment_content']=fav_comment_content[0]
			else:
				item['fav_comment_content']=''

			fav_comment_user_face = site.xpath('div/div[3]/div[1]/div/a/img/@src').extract()
			if len(fav_comment_user_face)>0:
				item['fav_comment_user_face'] = u'http:'+fav_comment_user_face[0]
			else:
				item['fav_comment_user_face'] = ''

			items.append(item)
		return items
