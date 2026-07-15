# app/scrapers/website_scraper.py

import requests
from bs4 import BeautifulSoup


class WebsiteScraper:

    @staticmethod
    def scrape(url: str):

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 Chrome/138 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        title = soup.title.string.strip() if soup.title else ""

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        # Detect websites that are blocking scraping
        blocked_keywords = [
            "captcha",
            "access denied",
            "verify you are human",
            "robot check",
            "forbidden",
        ]

        page = response.text.lower()

        if any(keyword in page for keyword in blocked_keywords):
            raise ValueError(
                "Website is blocking automated scraping."
            )

        # Validate extracted content
        if len(text) < 100:
            raise ValueError(
                "Very little content was extracted. "
                "The website may require JavaScript or be blocking requests."
            )

        return {
            "title": title,
            "html": response.text,
            "text": text,
        }