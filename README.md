# Rufus Scraper: AI-Powered Web Scraping & RAG Integration

Rufus is an advanced web scraping tool designed for retrieving, filtering, and ranking relevant web content. It integrates with retrieval-augmented generation (RAG) pipelines, making it ideal for AI-driven applications.


## Features

- Web Scraping: Uses Scrapy for structured data extraction.
- Text Processing: Cleans and filters irrelevant text using BeautifulSoup & regex.
- NLP Ranking: Implements sentence-transformers to rank text relevance.
- FastAPI: Provides a REST API for seamless integration.
- Output Formats: Supports JSON & CSV file downloads.
- Containerized Deployment: Ready to run with Docker.


## Installation & setup

1. Clone the repository
```bash
git clone https://github.com/shreyas-chigurupati07/rufus_web_crawler.git
cd rufus_web_crawler
```

2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```


## Running Rufus API
Start FastAPI Server
```bash
uvicorn rufus_api:app --host 0.0.0.0 --port 8000 --reload
```
API Docs: Visit http://127.0.0.1:8000/docs to test endpoints.

Scraping Websites:
Example API Call (Scrape a website):
```bash
curl -X 'POST' 'http://127.0.0.1:8000/scrape/' \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://news.ycombinator.com", "query": "AI"}'
```

Python Request Example:
```python
import requests

url = "https://news.ycombinator.com/"
query = "latest AI news"

response = requests.post("http://127.0.0.1:8000/scrape/", json={"url": url, "query": query})
print(response.json())
```

## Download Scraped Data
JSON Format:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/download/json'
```

CSV Format:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/download/csv'
```
