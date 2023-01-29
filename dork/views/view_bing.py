from .view_base import ViewBase
from .view_dork import ViewDork


class ViewBing(ViewBase, ViewDork):
    def __init__(self) -> None:
        super().__init__()

    def title(self, title: str)->None:
        print(self.fore.RED + f'[+*+]Title: {title}' + self.fore.RESET)

    def link(self, link: str)->None:
        print(self.fore.CYAN + f'[/-\]Link: {link}' + self.fore.RESET)

    def user_agent(self, user_agent: str)->None:
        print(self.fore.GREEN +
              f'[*-*]User agent: {user_agent}' + self.fore.RESET)

    def url(self, url: str) -> None:
        print(self.fore.YELLOW + f'[+*-*+]Url: {url} ' + self.fore.RESET)
