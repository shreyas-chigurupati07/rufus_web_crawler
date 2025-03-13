import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.rufus_crawler import RufusSpider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from scrapy import signals


# Global list to store extracted data
scraped_data = []

def collect_data(item, response, spider):
    """Collect scraped data into a global list"""
    scraped_data.append(item)

def run_spider(start_url):
    """Runs Scrapy spider and returns extracted data"""
    global scraped_data
    scraped_data = []  
    domain = start_url.split("//")[1].split("/")[0]

    # Create Scrapy runner
    runner = CrawlerRunner(get_project_settings())

    # Connect signal to collect data
    dispatcher.connect(collect_data, signal=signals.item_scraped)

    # Run the spider and collect results
    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(RufusSpider, start_url=start_url, allowed_domains=[domain])
        reactor.stop()

    reactor.callWhenRunning(crawl)
    reactor.run()  # Blocks execution until crawling is done

    return scraped_data

if __name__ == "__main__":
    start_url = "https://news.ycombinator.com/"
    #start_url = "https://www.bestbuy.com/site/searchpage.jsp?st=laptop"
    data = run_spider(start_url)
    print("Extracted Data:", data)