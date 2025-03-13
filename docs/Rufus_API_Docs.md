# **Rufus Web Scraper Documentation**

Version: 1.0
Last Updated: March 2025
Author: Shreyas Chigurupati


# Table of Contents
1. Introduction
2. Architecture Overview
3. Installation Guide
4. API Reference
5. Scraper Design
6. Natural Language Processing (NLP) Module
7. Data Storage & Formatting
8. Integration with RAG Pipelines
9. Deployment (Docker & Cloud)


## 1. Introduction

### 1.1 What is Rufus Scraper?

Rufus Scraper is an AI-powered web scraping framework designed for automated data extraction, intelligent filtering, and seamless integration into Retrieval-Augmented Generation (RAG) pipelines. It provides:
*	Efficient web crawling using Scrapy
*   Text extraction and cleaning using NLP techniques
*   Similarity-based ranking using transformer models
*   FastAPI-based REST API for easy integration
*   Structured JSON & CSV outputs

### 1.2 Key Use Cases
-   Automated content retrieval for LLMs
-   Building AI-driven chatbots with live data
-   Scraping product pricing for market analysis
-   Extracting financial or government data for research
-   Generating training datasets for NLP models

## 2. Architecture Overview

Rufus Scraper follows a modular architecture comprising multiple layers for scalability, flexibility, and ease of integration.

### 2.1 System Components
| Module | Description |
|-----------|----------|
| Scrapy-based Crawler | Fetches web pages and extracts raw content |
| NLP Processing (Sentence Transformers) | Filters and ranks text for relevance |
| FastAPI API Server | Exposes REST endpoints for data retrieval |
| Data Formatter (JSON/CSV) | FStores and structures extracted information |
| Dockerized Deployment | Ensures portable and scalable execution |


### 2.2 High-Level System Flow
	1.	User submits a URL and query via API
	2.	Scrapy crawler fetches web content
	3.	Text is cleaned and filtered using NLP
	4.	Relevant data is ranked and structured
	5.	Results are stored in JSON/CSV and served via API

### 2.3 Technology Stack
	•	Python 3.10+
	•	Scrapy (Web crawling)
	•	BeautifulSoup4 (HTML Parsing)
	•	FastAPI (REST API)
	•	Sentence-Transformers (NLP)
	•	FAISS (Optional - vector search)
	•	Docker (Containerized execution)


## 3. Installation Guide

### 3.1 Prerequisites

Ensure you have the following installed:
*   Python 3.10+
*   pip package manager
*   Docker (Optional for containerized deployment)

### 3.2 Setup Steps

- Step 1: Clone the Repository
```bash
git clone [your-repo-link]
cd rufus_scraper
```


- Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)
```

- Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

- Step 4: Start the API Server
```bash
uvicorn rufus_api:app --host 0.0.0.0 --port 8000 --reload
```

- API Docs Available at: http://127.0.0.1:8000/docs



4. API Reference

Rufus Scraper exposes a FastAPI-based RESTful API to interact with the system. Below are the available endpoints and their descriptions.

4.1 Base URL: http://127.0.0.1:8000/

4.2 Endpoints

4.2.1 Scrape a Website
	•	Endpoint: POST /scrape/
	•	Description: Crawls the specified website, extracts relevant text, and ranks content based on query relevance.
	•	Request Body:
        ```json
        {
            "url": "https://example.com",
            "query": "AI advancements"
        }
        ```
    •	Response:
        ```json
        {
            "message": "Scraping completed!",
            "data": [
                {
                    "url": "https://example.com",
                    "title": "Example Page",
                    "text": ["Extracted relevant content..."]
                }
            ]
        }

4.2.2 Download Extracted Data
	•	Endpoint: GET /download/{file_type}/
	•	Description: Allows downloading scraped data in JSON or CSV format.
	•	Parameters:
	•	file_type: (json or csv)
	•	Example Request:
        ```bash
        curl -X 'GET' 'http://127.0.0.1:8000/download/json'
        ```
    •	Response:
        ```json
        {
            "message": "Download JSON file at output.json"
        }
        ```


5. Scraper Design

5.1 Scrapy Spider Architecture

The Rufus Scraper is built using Scrapy, a powerful Python framework for web crawling.

| Component | Purpose |
|-----------|----------|
| RufusSpider | Main crawling class extending Scrapyâ€™s Spider class |
| clean_text() | Removes unnecessary content, formats text |
| parse() | Extracts structured data from web pages |
| clean_links() | Normalizes and filters links before following them |
| errback() | Handles failed requests gracefully |

5.2 Scrapy Spider Code

Please refer to the File at: src/rufus_crawler.py



6. NLP Processing & Data Storage

Rufus Scraper integrates Natural Language Processing (NLP) techniques to refine extracted text and make it query-relevant.

6.1 NLP Pipeline Overview

The NLP pipeline ensures that only relevant and meaningful content is retained.

| Step | Description |
|-----------|----------|
| Text Splitting | Breaks extracted text into chunks for processing |
| Embedding Generation | Converts text into vector representations |
| Relevance Ranking | Finds the most relevant sections based on user query |
| Summarization (Optional)| Uses LLMs (GPT) to generate a concise summary |

Please refer to the File at: src/rufus_nlp.py


6.2 Embedding & Ranking
	•	Text embeddings are generated using all-MiniLM-L6-v2, a SentenceTransformer model optimized for semantic search.
	•	Query-based cosine similarity is used to rank the most relevant content.

 Tech Stack:
	•	SentenceTransformers
	•	FAISS (for fast similarity search)
	•	Langchain RecursiveCharacterTextSplitter


6.3 Data Storage Formats

Rufus stores extracted data in multiple formats to support flexible integration into RAG pipelines and external applications.

| Storage Format | Use Case |
|-----------|----------|
| JSON (output.json) | Structured storage for NLP processing |
| CSV (output.csv) | Tabular format for easier analysis |

Please refer to the File at: src/rufus_formatter.py


7. RAG Pipeline Integration

Rufus is designed for Retrieval-Augmented Generation (RAG) systems, making it seamlessly compatible with LLM-based applications.

⸻

7.1 Steps to Integrate Rufus in RAG
	1.	Crawl & Extract Data
	•	Rufus scrapes content from a target website.
	2.	Process & Filter Text
	•	The NLP pipeline cleans and ranks relevant content.
	3.	Store in a Vector Database
	•	Rufus outputs data in JSON format, which can be indexed in FAISS, Chroma, Weaviate, etc.
	4.	Retrieve and Generate Responses
	•	When queried, embeddings are matched to the most relevant content, and responses are generated using LLMs (GPT, Claude, Gemini, etc.).

⸻

7.2 Example RAG Flow Using Rufus + FAISS
	•	Extract Data → Convert to Embeddings → Store in FAISS → Query for Contextual Retrieval
	•	This setup enhances LLM accuracy by grounding responses in relevant, real-world data.

 Integration Guide:
	1.	Run rufus_api.py to extract text.
	2.	Load JSON output into a vector store.
	3.	Use LLMs to generate informed responses.

 Recommended Stack:
	•	FAISS, ChromaDB for retrieval
	•	LangChain for LLM integration
	•	OpenAI API or Hugging Face Transformers for response generation








# **Rufus Web Scraper Documentation**

## **📌 Overview**
Rufus is an advanced web scraping framework designed to extract structured data from websites. It is built with **Scrapy** for efficient crawling and **FastAPI** to provide a RESTful API for managing scraping requests. The extracted content can be processed, filtered, and saved in **JSON** or **CSV** formats, making it ideal for **Retrieval-Augmented Generation (RAG) pipelines**.

---
## **🛠️ Features**
- **Fast & Scalable Web Crawling** using **Scrapy**
- **NLP Processing & Filtering** with **SentenceTransformers**
- **REST API for Scraping** using **FastAPI**
- **Storage Options:** JSON & CSV
- **Docker Support** for easy deployment
- **Customizable Query-Based Content Extraction**
- **Error Handling & Logging**

---
## **📂 Project Structure**
```
rufus_web_crawler/
│── src/
│   ├── rufus_crawler.py        # Web Scraping Logic (Scrapy Spider)
│   ├── rufus_nlp.py            # NLP-based Text Processing & Ranking
│   ├── rufus_formatter.py      # Data Formatting (JSON, CSV)
│── scripts/
│   ├── run_spider.py           # Script to Execute Scraper
│── tests/
│   ├── test_api.py             # API Testing
│── rufus_api.py                # FastAPI Application
│── Dockerfile                   # Docker Containerization
│── requirements.txt             # Dependencies
│── README.md                    # Project Guide
```

---
## **🚀 Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/rufus_web_crawler.git
cd rufus_web_crawler
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run FastAPI Server**
```sh
uvicorn rufus_api:app --host 0.0.0.0 --port 8000 --reload
```

---
## **📡 API Endpoints**

### **1️⃣ Web Scraping Request**
**Endpoint:** `/scrape/` (POST)
```json
{
  "url": "https://example.com",
  "query": "latest tech news"
}
```
**Response:**
```json
{
  "message": "Scraping completed!",
  "data": [
    {
      "url": "https://example.com/article1",
      "title": "Sample Article",
      "text": ["Extracted content here..."]
    }
  ]
}
```

### **2️⃣ Download Extracted Data**
**JSON:** `/download/json` (GET)
**CSV:** `/download/csv` (GET)

---
## **🐳 Running with Docker**
### **1️⃣ Build the Docker Image**
```sh
docker build -t rufus-web-crawler .
```

### **2️⃣ Run the Container**
```sh
docker run -p 8000:8000 rufus-web-crawler
```

### **3️⃣ Test the API**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/scrape/' -H 'Content-Type: application/json' -d '{"url": "https://example.com", "query": "sample query"}'
```

---
## **📑 How Rufus Works in a RAG Pipeline**
1. **Scrape** raw content from the target website.
2. **Process & Filter** relevant text based on the given query.
3. **Generate embeddings** using **SentenceTransformers**.
4. **Store embeddings** in a vector database like **FAISS**.
5. **Retrieve & Rank** relevant text chunks for downstream applications.

---
## **📌 Challenges & Solutions**
| Challenge | Solution |
|-----------|----------|
| JavaScript-heavy pages | Used Playwright for rendering |
| Extracting meaningful content | Used **NLP-based ranking** & filtering |
| Preventing duplicate links | Implemented URL normalization & deduplication |
| Handling pagination | Followed structured pagination rules |

---
## **📜 License**
Rufus is open-source under the **MIT License**.

---
## **📞 Support & Contribution**
- **GitHub Issues:** Report bugs or request features.
- **Pull Requests:** Contributions are welcome!
- **Contact:** Reach out via email or GitHub discussions.


