import bs4
import requests


class ProductionService:
    def __init__(self):
        pass

    @staticmethod
    def get_production_data(year: int) -> bs4.BeautifulSoup:
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_02"
        response = requests.get(url).content
        soup = bs4.BeautifulSoup(response, "lxml")
        table = soup.find("table", class_="tb_dados")
        return table

    @staticmethod
    def parse(table: bs4.BeautifulSoup):
        target_rows = table.select(
            'tr:has(td.tb_subitem:nth-child(1))'
            ':has(td.tb_subitem:nth-child(2))'
        )
        data = {}
        for row in target_rows:
            cells = row.find_all('td', class_='tb_subitem')
            if len(cells) == 2:
                product = cells[0].text.strip()
                quantity = cells[1].text.strip()
                data[product] = quantity
        return data
