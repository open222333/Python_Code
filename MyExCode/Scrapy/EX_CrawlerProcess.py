"""我們可以利用 scrapy.crawler.CrawlerProcess 這個類別來啟動爬蟲，scrapy crawl 指令其實也是使用這個類別。"""

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# https://docs.scrapy.org/en/latest/topics/api.html?highlight=CrawlerProcess#scrapy.crawler.CrawlerProcess

'''
get_project_settings() 方法會取得爬蟲專案中的 settings.py 檔案設定
啟動爬蟲前要提供這些設定給 Scrapy Engine
'''
process = CrawlerProcess(get_project_settings())
print(process)
# process.crawl('ithome')
# process.start()
