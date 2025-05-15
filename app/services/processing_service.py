from app.services.parsing_service import ParsingService


class ProcessingService:
    def __init__(self):
        self.url = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&subopcao={}&opcao=opt_03"

    @staticmethod
    def parse_option(option: int) -> str:
        return f"subopt_0{option}"

    def get_processing_data(self, year: int, option: int) -> list:
        parsed_option = self.parse_option(option)
        url = self.url.format(year, parsed_option)
        ps = ParsingService(url)
        processing_data = ps.get_data()
        return processing_data
