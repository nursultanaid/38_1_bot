# import requests
# from parsel import Selector
#
#
# class FilmScraper:
#     URL = 'https://rezka.ag/'
#
#     HEADERS = {
#         "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"
#
#     }
#     LINK_XPATH = '//div[@class="b-content__inline_item"]/div[@class="b-content__inline_item-link"]/a/@href'
#     IMG_XPATH = '//div[@class="b-content__inline_item-cover"]/a/img[@src]'
#     TITLE_XPATH = '//div[@class="b-content__inline_item-link"]/a/text()'
#     DESC_XPATH = '//div[@class="b-content__inline_item-link"]/div/text()'
#
#     def true_link(self, links):
#         for i in range(0, len(links)):
#             if not links[i].startswith('https://rezka.ag'):
#                 links[i] = 'https://rezka.ag/'.join(links[i])
#         return links
#
#     def scrape_data(self):
#         response = requests.request(method="GET", url=self.URL, headers=self.HEADERS)
#         # print(response.text)
#         tree = Selector(text=response.text)
#         new_links = tree.xpath(self.LINK_XPATH).getall()
#         links = [i for i in new_links if i.startswith('https://rezka.ag/')]
#         images = tree.xpath(self.IMG_XPATH).getall()
#         titles = tree.xpath(self.TITLE_XPATH).getall()
#         descs = tree.xpath(self.DESC_XPATH).getall()
#
#         return_data = []
#         for i in range(0, len(links)):
#             data = {}
#             data['link'] = links[i]
#             data['image'] = images[i]
#             data['title'] = titles[i]
#             data['desc'] = descs[i]
#             return_data.append(data)
#         return return_data
#
# if __name__ == "__main__":
#     scraper = FilmScraper()
#     print(scraper.scrape_data())