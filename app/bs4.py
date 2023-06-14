import scrapy


class GoogleSearchSpider(scrapy.Spider):
    name = 'google_search'
    start_urls = ['https://www.google.com/search?q=']

    def parse(self, response):
        # Find all div elements
        div_elements = response.css('div')
        for div in div_elements:
            span_elements = div.css('span[aria-hidden="true"][class="oqSTJd"]')
            for span in span_elements:
                score_text = span.css('::text').get().strip()
                review_score = score_text.split('/')[0]
                if review_score is None:
                    review_score = ""
                yield {"review_score": review_score}

