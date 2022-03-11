import scrapy

QUERY = "q=kw%3A*&fq=%28%28x0%3Abook+x4%3Aprintbook%29%29+>+yr%3A2019+>++>+ln%3Adut+>+fm%3Afic&dblist=638"

class Spider(scrapy.Spider):
    name = 'worldcatspider'
    start_urls = ['https://www.worldcat.org/search?start=%s&%s' % (number, QUERY) for number in range(0, 4400, 10)]

    def parse(self, response):
        for searchResult in response.css('.menuElem'):
            author = searchResult.css('.author ::text').get()

            # Remove 'by ' if the author field starts with that prefix
            if author[0:3] == "by ":
                author = author[3:]

            yield {
                "title:": searchResult.css('.name a > strong ::text').extract(),
                "author:": author,
                "publisher:": searchResult.css('.publisher span ::text').extract(),
            }

        # for next_page in response.css('a.next-posts-link'):
        #    yield response.follow(next_page, self.parse)