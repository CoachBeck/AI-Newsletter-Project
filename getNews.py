import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_articles(query="technology", num_articles=5):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&pageSize={num_articles}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    articles = []
    for article in data.get("articles", []):
        content = article.get("content") or article.get("description") or ""
        if content:
            articles.append({
                "title": article["title"],
                "url": article["url"],
                "content": content
            })

    return articles