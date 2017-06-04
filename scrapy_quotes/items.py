# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScrapyQuotesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tags = Field()
    text = Field()
    author = Field()
    born = Field()
    description = Field()
