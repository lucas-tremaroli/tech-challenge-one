class UrlService:
    def __init__(self):
        pass

    @staticmethod
    def parse_option(option: int) -> str:
        return f"subopt_0{option}"

    def parse_url(self, target: str, year: int, option: int = 0) -> str:
        if option > 0:
            parsed_option = self.parse_option(option)
            return target.format(year, parsed_option)
        return target.format(year, option)
