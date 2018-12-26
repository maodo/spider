# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JumiaItem(scrapy.Item):
    # define the fields for your item here like:
    marque = scrapy.Field()
    #modele = scrapy.Field()
    boite_de_vitesse = scrapy.Field()
    kilometrage = scrapy.Field()
    annee = scrapy.Field()
    type_de_carburant = scrapy.Field() 
    prix = scrapy.Field()
    #carosserie = scrapy.Field()
    #image_url = scrapy.Field()
