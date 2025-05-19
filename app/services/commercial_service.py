from app.services.parsing_service import ParsingService


class CommercialService:
    def __init__(self):
        self.url = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&opcao=opt_04"

    def get_commercial_data(self, year: int) -> list:
        url = self.url.format(year)
        ps = ParsingService(url)
        commercial_data = ps.get_data()
        return commercial_data
