from enum import Enum


class EndpointEnum(str, Enum):
    """
    Enum for the endpoints of the API.
    """
    production = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&opcao=opt_02"
    processing = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&subopcao={}&opcao=opt_03"
    commercial = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&opcao=opt_04"
