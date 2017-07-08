import scrapy
import json

file_name = "monstersSlug.json"
base_url = "https://www.dndbeyond.com/monsters/{}"

class BlogSpider(scrapy.Spider):
    name = 'monster_get_info'
    start_urls = ['https://www.dndbeyond.com/monsters?page=1']

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUEST_PER_DOMAIN": 1
    }

    def __init__(self):
        self.start_urls = []

        with open(file_name) as slug_file:
            slug_data = json.load(slug_file)
            for slug_info in slug_data:
                monster_url = base_url.format(slug_info['slug'])
                self.start_urls.append(monster_url)

    def parse(self, response):

        MONSTER_SELECTOR = '.monster-name ::text'

        yield {
            'name': response.css(MONSTER_SELECTOR).extract_first().strip(),
        }



