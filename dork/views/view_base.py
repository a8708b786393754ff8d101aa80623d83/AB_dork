from colorama import Fore
from colorama import Back


class ViewBase(object):
    def __init__(self) -> None:
        self.fore = Fore
        self.back = Back

    def banner(self) -> None:
        print(f"""
        BANNIERE
        """)

    def query(self, query: dict):
        print(self.back.LIGHTRED_EX + self.fore.WHITE +
              f'Query: {query}' + self.fore.RESET + self.back.RESET)

    def start_msg(self):
        print(self.back.YELLOW + self.fore.BLUE +
              'message' + self.fore.RESET + self.back.RESET)
