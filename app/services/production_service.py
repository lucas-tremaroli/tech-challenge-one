# This module contains the business logic for scrapping the production data.

import bs4
import requests


def get_production_data(year: int) -> bs4.BeautifulSoup:
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_02"
    response = requests.get(url).content
    soup = bs4.BeautifulSoup(response, "lxml")
    table = soup.find("table", class_="tb_dados")
    return table
