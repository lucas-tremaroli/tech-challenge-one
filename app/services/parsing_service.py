import bs4
import requests


class ParsingService:
    def __init__(self, url: str):
        self.url = url

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
        print(category)
        return category.lower()

    def parse(self, table: bs4.BeautifulSoup) -> list:
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

    def get_data(self) -> list:
        response = requests.get(self.url).content
        soup = bs4.BeautifulSoup(response, "lxml")
        table = soup.find("table", class_="tb_dados")
        parsed_data = self.parse(table)
        return parsed_data
