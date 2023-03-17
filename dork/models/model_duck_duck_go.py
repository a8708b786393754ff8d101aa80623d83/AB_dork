from .model_base import ModelBase
from .model_dork import ModelDork

import bs4


class ModelDuckDuckGo(ModelBase, ModelDork):
    """Classe model des donnée de duckduckgo.

    Args:
        ModelBase (object): model de base
        ModelDork (object): model des dorks
    """

    def __init__(self) -> None:
        """Methode constructrice."""

        super().__init__()
        self.navigator = 'duckduckgo'
        self.search_engine = 'duckduckgo'


    def get_link(self, div: bs4.element.Tag) -> str:
        """Recupere le lien

        Args:
            div (bs4.element.Tag): balise div HTML

        Returns:
            str: lien de la balise a.
        """

        return div.h2.a['href']

    def get_title(self, div: bs4.element.Tag) -> str:
        """Recupere le titre

        Args:
            div (bs4.element.Tag): balise div HTML

        Returns:
            str: titre de la balise a.
        """

        return div.h2.a.span.text

    def get_main_node(self, soup: bs4.BeautifulSoup) -> list[bs4.element.Tag]:
        """Recupere le noeud main

        Args:
            soup (bs4.BeautifulSoup): soup de la page 

        Returns:
            list: données. 
        """

        return soup.find_all('article')
