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

    def blocks_request(self) -> bool: pass

    def get_link(self, div: bs4.element.Tag) -> str:
        """Recupere le lien

        Args:
            div (bs4.element.Tag): balise div HTML

        Returns:
            str: lien de la balise a.
        """

        return super().get_link(div)

    def get_title(self, div: bs4.element.Tag) -> str:
        """Recupere le titre

        Args:
            div (bs4.element.Tag): balise div HTML

        Returns:
            str: titre de la balise a.
        """

        return super().get_title(div)

    def get_main_node(self, soup: bs4.BeautifulSoup) -> list:
        """Recupere tout les informations 

        Args:
            soup (bs4.BeautifulSoup): soup de la page 

        Returns:
            list: données. 
        """

        raise NotImplementedError
