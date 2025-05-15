from app.services.parsing_service import ParsingService


class ProcessingService:
    def __init__(self):
        self.url = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&subopcao={}&opcao=opt_03"

    def get_processing_data(self, year: int, opt: str) -> list:
        url = self.url.format(year, opt)
        ps = ParsingService(url)
        processing_data = ps.get_data()
        return processing_data
