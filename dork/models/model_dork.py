from abc import ABC, abstractmethod

import bs4
# first=61&FORM=PERE3

class ModelDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def blocks_request(self) -> bool: pass

    @abstractmethod
    def get_link(self, div: bs4.element.Tag) -> str: pass

    @abstractmethod
    def get_title(self, div: bs4.element.Tag) -> str: pass

    @abstractmethod
    def get_all(self, soup: bs4.BeautifulSoup) -> list: pass
