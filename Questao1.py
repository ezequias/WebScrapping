import scrapy
from scrapy.shell import inspect_response
import re

# Forma de executar o programa
# scrapy runspider Questao1.py --nolog

class UolSpider(scrapy.Spider):
    name = "Uol"

    start_urls = {
        'https://www.uol.com.br'
    }

    def parse (self, response):
        valor = response.css(".HU_currency__quote_up::text").extract_first()

        if valor is None:
            valor = response.css(".HU_currency__quote_down::text").extract_first()
        
        print("A cotação atual do dólar é: R$ {}".format(valor))
