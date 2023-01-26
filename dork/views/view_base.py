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

    def start_msg(self):
        print(self.back.YELLOW + self.fore.BLUE +
              'message' + self.fore.RESET + self.back.RESET)
