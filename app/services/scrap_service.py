import bs4
import json
import logging
import requests
from app.core.cache import Cache

logger = logging.getLogger(__name__)


class ScrapService:
    def __init__(self):
        self.cache = Cache()

    @staticmethod
    def parse_quantity(qtd: str) -> int:
        qtd = qtd.replace('.', '')
        qtd = qtd.replace('-', '0')
        return int(qtd)

    @staticmethod
    def parse_category(category: str) -> str:
        category = category.replace(' ', '_')
        category = category.replace('(', '')
        category = category.replace(')', '')
        category = category.replace(',', '')
        return category.lower()

    def parse(self, table) -> list:
        rows = table.tbody.find_all('tr')
        data = []
        category = None
        for row in rows:
            cells = row.find_all('td')
            product = cells[0].get_text(strip=True)
            quantity = cells[1].get_text(strip=True)
            if row.find('td', class_='tb_item'):
                category = self.parse_category(product)
            else:
                aux = dict()
                aux["category"] = category
                aux["subcategory"] = self.parse_category(product)
                aux["quantity"] = self.parse_quantity(quantity)
                data.append(aux)
        return data

    def get_data(self, url: str):
        try:
            response = requests.get(url).content
        except requests.exceptions.ConnectionError:
            logger.error(f"Failed to connect to the URL: {url}")
            cached_data = self.cache.fallback(url)
            if cached_data:
                logger.warning("Returning cached data after connection error")
                return cached_data
            logger.error("No cached data available, returning exception")
            return Exception("Failed to connect to the URL")
        soup = bs4.BeautifulSoup(response, "lxml")
        table = soup.find("table", class_="tb_dados")
        parsed_data = self.parse(table)
        self.cache.set(url, str(parsed_data))
        return parsed_data
