from abc import ABC, abstractmethod

import bs4


class ModelDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def blocks_request(self) -> bool: pass

    @abstractmethod
    def get_user_agent(self) -> str: pass

    @abstractmethod
    def get_link_search(self) -> str: pass

    @abstractmethod
    def get_link(self, div: bs4.element.Tag) -> str: pass

    @abstractmethod
    def get_title(self, div: bs4.element.Tag) -> str: pass

    @abstractmethod
    def get_all(self, soup: bs4.BeautifulSoup) -> list: pass
