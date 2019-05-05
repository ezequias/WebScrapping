import scrapy
from scrapy.shell import inspect_response
import re

# A chamada para a execução deste programa é:
# scrapy runspider -a category=bola Questao2.py --nolog

class MLSpider(scrapy.Spider):
    name = "Mercado Livre"

    def __init__(self, category=None, *args, **kwargs):
        start_urls = {
            'https://lista.mercadolivre.com.br/' + category + '#D[A:' + category
        }
        super(MLSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        i = 0
        itens = response.css('.item__info')

        for item in itens:
            if len(item.css('.item__price::text').extract())> 2:
                print (item.css('.main-title::text').extract_first() + " - " + item.css('.price__fraction::text').extract_first() + "," + item.css('.price__decimal::text').extract_first())
            else:
                print (item.css('.main-title::text').extract_first() + " - " + item.css('.price__fraction::text').extract_first() + ",00")