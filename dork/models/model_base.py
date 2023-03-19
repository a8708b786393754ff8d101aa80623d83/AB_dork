import requests
from bs4 import BeautifulSoup
import dork.const as const

from .extension.ModelExtensionJson import ModelExtensionJson
from .extension.ModelExtensionYaml import ModelExtensionYaml


class ModelBase:
    """Model de base."""

    def __init__(self) -> None:
        """Methode constructrice."""

        self.navigator = ''
        self.search_engine = ''
        self.message_blocks = ''
        self.operator_dork = ''

        self.const = const
        self.init_operator()

    def get_link_search(self) -> str:
        """Recupere le lien de recherche de google

        Returns:
            str: lien de recherche de google
        """

        data = ModelExtensionJson.get_content_file(
            self.const.PATH_DATA + self.const.FILENAME_LINKS)
        return data[self.search_engine]

    def init_operator(self):
        """Ajoute a l'attribut operator une liste des operateur dork."""

        self.operator_dork = ModelExtensionJson.get_content_file(
            self.const.PATH_DATA + self.const.FILENAME_DORK)['dork']
        
    def get_header(self): 
        """Recupere le header a partir d'un fichier."""
        
        return ModelExtensionYaml.get_content_file(self.const.PATH_DATA + self.const.FILENAME_HEADERS)[self.navigator]

    def get_soup(self, resp: requests.Response) -> BeautifulSoup:
        """Recupere le soup d'une page html

        Args:
            resp (requests.Response): reponse de la requete

        Returns:
            BeautifulSoup: soup du contenue de la page
        """

        return BeautifulSoup(resp.content, 'lxml') if resp.ok else None
