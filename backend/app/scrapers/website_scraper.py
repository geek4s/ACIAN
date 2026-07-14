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

        return {
            "title": soup.title.string if soup.title else "",
            "html": response.text,
            "text": soup.get_text(separator=" ", strip=True)
        }