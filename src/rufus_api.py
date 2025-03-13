from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
import os
import sys

# Ensure correct imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.run_spider import run_spider
from src.rufus_nlp import filter_relevant_text
from src.rufus_formatter import save_as_json, save_as_csv

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: str
    query: str


@app.post("/scrape/")
async def scrape(request: ScrapeRequest):
    """Crawl a website, filter relevant text, and return structured data."""
    try:
        raw_data = run_spider(request.url)
        
        if not raw_data:
            raise HTTPException(status_code=500, detail="No data extracted.")

        filtered_data = []
        for item in raw_data:
            processed_item = {
                "url": item["url"],
                "title": item["title"],
                "text": filter_relevant_text(item["text"], request.query)
            }
            filtered_data.append(processed_item)

            # Save partial data incrementally
            save_as_json(filtered_data, "output.json")
            save_as_csv(filtered_data, "output.csv")

        return {"message": "Scraping completed!", "data": filtered_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/download/{file_type}")
async def download(file_type: str):
    """Allows users to download scraped content in JSON or CSV."""
    file_map = {
        "json": "output.json",
        "csv": "output.csv",
    }

    file_path = file_map.get(file_type)
    
    if file_path and os.path.exists(file_path):
        return FileResponse(path=file_path, filename=file_path, media_type="application/octet-stream")
    
    raise HTTPException(status_code=404, detail="File not found")