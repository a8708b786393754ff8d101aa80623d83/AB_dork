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


    def get_link(self, li: bs4.element.Tag) -> str:
        """Recupere le lien

        Args:
            li (bs4.element.Tag): balise li HTML

        Returns:
            str: lien de la balise a.
        """

        return li.h2.a['href']

    def get_title(self, li: bs4.element.Tag) -> str:
        """Recupere le titre

        Args:
            li (bs4.element.Tag): balise li HTML

        Returns:
            str: titre de la balise a.
        """
        return li.h2.text

    def get_main_node(self, soup: bs4.BeautifulSoup) -> list[bs4.element.Tag]:
        """Recupere le noeud main

        Args:
            soup (bs4.BeautifulSoup): soup de la page 

        Returns:
            list: données. 
        """

        return soup.select('main > ol > li')
