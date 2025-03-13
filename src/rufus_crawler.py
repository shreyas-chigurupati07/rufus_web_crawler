import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re

class RufusSpider(scrapy.Spider):
    name = "rufus"

    def __init__(self, start_url, allowed_domains, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = allowed_domains
        self.visited_urls = set()

    def clean_text(self, html_text):
        """ Removes HTML tags, timestamps, vote counts, and metadata """
        soup = BeautifulSoup(html_text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)

        # Remove login prompts, vote counts, timestamps, and metadata
        text = re.sub(r'\b(login|hide|favorite|points|comments|reply|past|ask|show|submit)\b', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\d+ (points?|comments?)', '', text)  # Remove "123 points" / "45 comments"
        text = re.sub(r'\d+ (hours?|days?|minutes?) ago', '', text)  # Remove timestamps like "2 hours ago"
        text = re.sub(r'\s*\|\s*', ' ', text)  # Remove unnecessary "|"
        text = re.sub(r'\s+', ' ', text).strip()  # Normalize spaces

        return text
    
    async def parse(self, response):
        """ Extract text, clean HTML, and follow valid links """
        url = response.url
        self.visited_urls.add(url)

        # Extract title
        title = response.xpath("//title/text()").get()

        # Extract and clean text content
        raw_text = " ".join(response.xpath("//p//text() | //div//text() | //span//text()").getall())
        text_content = self.clean_text(raw_text)

        # Extract links and filter them
        links = response.xpath("//a/@href").getall()
        cleaned_links = self.clean_links(response, links)

        yield {
            "url": url,
            "title": title.strip() if title else "No Title",
            "text": text_content if text_content else "No relevant content found.",
            "links": cleaned_links
        }

        # Follow new links
        for link in cleaned_links:
            if link not in self.visited_urls:
                self.visited_urls.add(link)
                yield scrapy.Request(url=link, callback=self.parse, errback=self.errback)


    def clean_links(self, response, links):
        """ Convert relative URLs to absolute, filter unwanted links, and remove tracking parameters """
        base_url = response.url
        absolute_links = [urljoin(base_url, link) for link in links if not link.startswith("javascript")]
        domain = urlparse(base_url).netloc

        # Remove unwanted links (e.g., voting, login, register, comments, tracking parameters)
        blocked_keywords = ["vote", "login", "register", "submit", "reply", "comment", "hide", "logout"]
        filtered_links = [
            re.sub(r'\?.*', '', link)  # Remove tracking parameters (everything after `?`)
            for link in absolute_links
            if urlparse(link).netloc == domain and not any(keyword in link.lower() for keyword in blocked_keywords)
        ]

        return list(set(filtered_links))  # Remove duplicates

    async def errback(self, failure):
        """ Error handling for failed requests """
        self.logger.error(f"Request failed: {failure.request.url} | Error: {failure.value}")