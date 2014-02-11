# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class YelpspiderItem(Item):
	name = Field()
	url = Field()
	address_l1 = Field()
	address_l2 = Field()
	category = Field()
	phone = Field()
	rating = Field()
	price_rating = Field()
	thumbUrl = Field()
	fav_comment_user = Field()
	fav_comment_content = Field()
	fav_comment_user_face = Field()
