"""
Scrapes data from http://www.imsdb.com/all%20scripts/
"""
import scrapy

INDEX_PAGE = "http://www.imsdb.com/all%20scripts"

BASE = "http://www.imsdb.com"

class ScriptMovieScrapey(scrapy.Spider):
    name = 'script-database'
    start_urls = [INDEX_PAGE]

    def parse(self, response):
        for href in response.css('a[href^="/Movie"]::attr(href)'):
            full_url = '%s%s' % (BASE, href.extract())
            yield scrapy.Request(full_url, callback=self.parse_script)

    def parse_script(self, response):
        script_link = \
            response.css('table.script-details a[href^="/scripts"]::attr(href)').extract()[0]
        url = '%s%s' % (BASE, script_link)
 
        request = scrapy.Request(url, callback=self.parse_question)
        request.meta['header'] = {
            'title': response.css('table.script-details h1::text').extract()[0],
            'raw_details': response.css('td').extract()[1],
            'genres': response.css('table.script-details a[href^="/genre"]::text').extract(),
            'writer': response.css('table.script-details a[href^="/writer"]::text').extract(),
            'link': response.css('table.script-details a[href^="/scripts"]::attr(href)').extract()[0],
            }
        yield request

    def parse_question(self, response):

        meta = response.meta['header']
        meta['raw_script'] = response.css('td.scrtext pre').extract()[0]

        yield meta

