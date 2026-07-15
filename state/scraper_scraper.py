from app.scrapers.website_scraper import WebsiteScraper

result = WebsiteScraper.scrape("https://openai.com")

print(result["title"])
print()
print(result["text"][:1000])