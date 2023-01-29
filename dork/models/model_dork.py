from abc import ABC, abstractmethod

import bs4


class ModelDork(ABC):
    """Classe model des dork

    Args:
        ABC (object): classe abs
    """

    def __init__(self) -> None:
        """Methode constructrice."""

        super().__init__()

    @abstractmethod
    def blocks_request(self) -> bool: ...

    @abstractmethod
    def get_link(self, div: bs4.element.Tag) -> str: ...

    @abstractmethod
    def get_title(self, div: bs4.element.Tag) -> str: ...

    @abstractmethod
    def get_main_node(self, soup: bs4.BeautifulSoup) -> list: ...
