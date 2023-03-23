from .model_base import ModelBase
from .model_dork import ModelDork

import bs4


class ModelGoogle(ModelBase, ModelDork):
    """Classe model des donnée de google.

    Args:
        ModelBase (object): model de base
        ModelDork (object): model des dorks
    """

    def __init__(self) -> None:
        """Methode constructrice."""

        super().__init__()
        self.navigator = 'chrome'
        self.search_engine = 'google'

    def get_sector_result(self, node: bs4.BeautifulSoup) -> bs4.ResultSet:
        """Renvoie la div qui contient les informations de chaqsue resultat

        Args:
            node (bs4.BeautifulSoup): noeud html

        Returns:
            bs4.ResultSet: object bs4
        """

        return node.find_all(class_='yuRUbf')

    def get_link(self, div: bs4.element.Tag) -> str:
        """Recupere le lien

        Args:
            div (bs4.element.Tag): balise div HTML

        Returns:
            str: lien de la balise a.
        """

        return div.a.get('href')

    def get_title(self, div: bs4.element.Tag) -> str:
        """Recupere le titre

        Args:
            div (bs4.element.Tag): balise div HTML

        Returns:
            str: titre de la balise h3.
        """

        return div.find('h3')

    def get_main_node(self, soup: bs4.BeautifulSoup) -> list:
        """Recupere tout les informations 

        Args:
            soup (bs4.BeautifulSoup): soup de la page 

        Returns:
            list: noeud principal ou est tout le resulta de la recherce. 
        """

        return soup.find(id="rso")
