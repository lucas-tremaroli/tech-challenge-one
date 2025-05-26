from enum import Enum
from pydantic import BaseModel


class EndpointEnum(str, Enum):
    """
    Enum for the endpoints of the API.
    """
    production = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&opcao=opt_02"
    processing = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&subopcao={}&opcao=opt_03"
    commercial = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&opcao=opt_04"
    importation = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&subopcao={}&opcao=opt_05"
    exportation = "http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&subopcao={}&opcao=opt_06"


class ConnectionError(BaseModel):
    """
    Model for connection error.
    """
    detail: str
