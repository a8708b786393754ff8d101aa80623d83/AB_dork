from .model_base import ModelBase
from .model_dork import ModelDork

import bs4


class ModelBing(ModelBase, ModelDork):
    """Classe model des donnée de bing.

    Args:
        ModelBase (object): model de base
        ModelDork (object): model des dorks
    """

    def __init__(self) -> None:
        """Méthode constructrice."""

        super().__init__()
        self.navigator = 'bingbot'
        self.search_engine = 'bing'

    def blocks_request(self) -> bool: pass

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

        return div.h2.a.text

    def get_main_node(self, soup: bs4.BeautifulSoup) -> list[bs4.element.Tag]:
        """Recupere le noeud main

        Args:
            soup (bs4.BeautifulSoup): soup de la page 

        Returns:
            list: données. 
        """

        return soup.select('main li')
