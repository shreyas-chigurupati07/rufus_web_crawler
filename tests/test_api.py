import requests
import os

url = "https://news.ycombinator.com/"
query = "latest tech news"

# Start scraping
response = requests.post("http://127.0.0.1:8000/scrape/", json={"url": url, "query": query})
print("Scraping Response:", response.json())

# Wait for scraping to finish (or manually check for output.json before running this)
if os.path.exists("output.json"):
    download_response = requests.get("http://127.0.0.1:8000/download/json")

    if download_response.status_code == 200:
        with open("tests/downloaded_output.json", "wb") as f:
            f.write(download_response.content)
        print("JSON File Downloaded Successfully!")
    else:
        print("Failed to download JSON file")
else:
    print("No JSON file found. The scraper might not have completed.")


# import requests
# import os

# url = "https://www.bestbuy.com/site/searchpage.jsp?st=laptop"
# query = "laptop prices"

# # Start scraping
# response = requests.post("http://127.0.0.1:8000/scrape/", json={"url": url, "query": query})
# print("Scraping Response:", response.json())

# # Wait for scraping to finish (or manually check for output.json before running this)
# if os.path.exists("output.json"):
#     download_response = requests.get("http://127.0.0.1:8000/download/json")

#     if download_response.status_code == 200:
#         with open("tests/downloaded_output.json", "wb") as f:
#             f.write(download_response.content)
#         print("JSON File Downloaded Successfully!")
#     else:
#         print("Failed to download JSON file")
# else:
#     print("No JSON file found. The scraper might not have completed.")