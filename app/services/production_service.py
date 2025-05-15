from app.services.parsing_service import ParsingService


class ProductionService:
    def __init__(self):
        self.url = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&opcao=opt_02"

    def get_production_data(self, year: int) -> list:
        url = self.url.format(year)
        ps = ParsingService(url)
        production_data = ps.get_data()
        return production_data
