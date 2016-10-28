# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider


class DaxSpider(CrawlSpider):
    name = "dax_top30"
    allowed_domains = ['www.finanzen.net/']
    start_urls = [
        "http://www.finanzen.net/index/DAX/30-Werte",
    ]
    items = []

    def parse(self, response):

        table = response.xpath(".//*[@id='mainWrapper']/div[3]/div[1]/div/table/tr")
        for item in table:
            if not item.xpath('./td/text()'):
                continue
            row = {}
            row['Name'] = self.safe_index(item.xpath('./td[1]/a[1]/text()').extract())
            row['ISIN'] = self.safe_index(item.xpath('./td[1]/a[2]/text()').extract())
            row['Letzter'] = self.safe_index(item.xpath('./td[2]/text()').extract())
            row['Vortag'] = self.safe_index(item.xpath('./td[2]/text()').extract(), i=1)
            row['Tief'] = self.safe_index(item.xpath('./td[3]/text()').extract())
            row['Hoch'] = self.safe_index(item.xpath('./td[3]/text()').extract(), i=1)
            row['+/-'] = self.safe_index(item.xpath('./td[5]/text()').extract())
            row['%'] = self.safe_index(item.xpath('./td[5]/text()').extract(), i=1)
            row['Zeit'] = self.safe_index(item.xpath('./td[7]/text()').extract())
            row['Datum'] = self.safe_index(item.xpath('./td[7]/text()').extract(), i=1)
            row['+/- 3 Mon.'] = self.safe_index(item.xpath('./td[8]/text()').extract())
            row['% 3 Mon.'] = self.safe_index(item.xpath('./td[8]/text()').extract(), i=1)
            row['+/- 6 Mon.'] = self.safe_index(item.xpath('./td[9]/text()').extract())
            row['% 6 Mon.'] = self.safe_index(item.xpath('./td[9]/text()').extract(), i=1)
            row['+/- 1 Jahr'] = self.safe_index(item.xpath('./td[10]/text()').extract())
            row['% 1 Jahr'] = self.safe_index(item.xpath('./td[10]/text()').extract(), i=1)
            self.items.append(row)

        for item in self.items:
            print item
        return

    def safe_index(self, l, i=0):
        """Handle base exceptions for access to the list
        """
        try:
            return l[i]
        except (IndexError, TypeError):
            return ''
