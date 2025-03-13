import requests
import os

class RufusClient:
    def __init__(self, base_url="http://127.0.0.1:8000", api_key=None):
        self.base_url = base_url
        self.api_key = api_key or os.getenv("RUFUS_API_KEY")

    def scrape(self, url, query):
        """ Sends a scraping request to the Rufus API """
        payload = {"url": url, "query": query}
        response = requests.post(f"{self.base_url}/scrape/", json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def download(self, file_type="json"):
        """ Downloads the scraped file in JSON, CSV, or PDF format """
        response = requests.get(f"{self.base_url}/download/{file_type}")

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

# Example usage
if __name__ == "__main__":
    client = RufusClient()
    instructions = "Find information about latest technology news."
    
    # Scrape news from Y Combinator
    documents = client.scrape("https://news.ycombinator.com/", instructions)
    print("Scraped Data:", documents)

    # Download results as JSON
    download_link = client.download("json")
    print("Download JSON:", download_link)