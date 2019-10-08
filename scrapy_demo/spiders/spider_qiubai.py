import scrapy


class QiuBai(scrapy.Spider):

    name = 'qiubai'
    allowed_domains = ['qiushibaike.com']

    headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0"
        }

    def start_requests(self):
        url = 'https://www.qiushibaike.com/8hr/page/{}/'

        yield scrapy.Request(url.format(1), callback=self.parse, headers=self.headers)

    def parse(self, response):

        item_temp = response.xpath(
            '//div[@class="recommend-article"]/ul/li[@class="item typs_word"]')
        # print(len(item_temp), item_temp)
        for item in item_temp:
            href = item.xpath('.//a[@class="recmd-content"]/@href').extract_first()
            content = item.xpath('.//a[@class="recmd-content"]/text()').extract_first()

            detail_url = response.urljoin(href)
            # print(href, content, detail_url)

            yield scrapy.Request(detail_url, callback=self.detail_content, headers=self.headers)

    def detail_content(self, response):

        content = response.xpath('//div[@class="content"]/node()').extract()
        # content = response.css('div.content::text').extract()
        # content = response.css('div.content::text').extract()
        print(content)