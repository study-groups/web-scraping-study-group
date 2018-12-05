# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class ScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RedditForum(Item):
    """Livingsocial container (dictionary-like object) for scraped data"""
    title = Field()
    link = Field()
    content = Field()