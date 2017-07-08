import scrapy
import urlparse

max_page = 37

## Good tutorial: https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
## Good to experiment: shell https://doc.scrapy.org/en/latest/topics/selectors.html

class BlogSpider(scrapy.Spider):
    name = 'monster_get_slug'
    start_urls = ['https://www.dndbeyond.com/monsters?page=1']

    custom_settings = {
        "DOWNLOAD_DELAY": 0,
        "CONCURRENT_REQUEST_PER_DOMAIN": 1
    }

    def parse(self, response):

        MONSTER_SELECTOR = 'div.info'

        for monster in response.css(MONSTER_SELECTOR):
            SLUG_SELECTOR = '::attr(data-slug)'
            NAME_SELECTOR = '.monster-name .name a ::text'

            yield {
                'name': monster.css(NAME_SELECTOR).extract_first(),
                'slug': monster.css(SLUG_SELECTOR).extract_first(),
            }

        url = urlparse.urlparse(response.url)
        params = urlparse.parse_qs(url.query)

        currentPage = int(params['page'][0])

        if currentPage <= max_page:
            yield scrapy.Request(
                response.urljoin('/monsters?page={}'.format(currentPage + 1))
            )
