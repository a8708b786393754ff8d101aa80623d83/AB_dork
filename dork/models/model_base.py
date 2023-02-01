import json
import random
from pathlib import Path

import requests
from bs4 import BeautifulSoup

import dork.const as const


class ModelBase(object):
    """Model de base. 

    Args:
        object (_type_): objet 
    """

    def __init__(self) -> None:
        """Methode constructrice."""

        self.navigator = ''
        self.search_engine = ''
        self.message_blocks = ''
        self.operator_dork = ''

        self.const = const

    def get_link_search(self) -> str:
        """Recupere le lien de recherche de google

        Returns:
            str: lien de recherche de google
        """

        data = self.get_content_file(
            self.const.PATH_DATA + self.const.FILENAME_LINKS)
        return data[self.search_engine]

    def get_user_agent(self) -> str:
        """Recupere un user agent 

        Returns:
            str: user agent
        """

        data = self.get_content_file(
            self.const.PATH_DATA + self.const.FILENAME_USER_AGENT)
        return random.choice(data[self.navigator])

    def set_operator(self):
        """Ajoute a l'attribut operator une liste des operateur dork."""

        self.operator_dork = self.get_content_file(
            self.const.PATH_DATA + self.const.FILENAME_DORK)

    def get_soup(self, resp: requests.Response) -> BeautifulSoup:
        """Recupere le soup d'une page html

        Args:
            resp (requests.Response): reponse de la requete

        Returns:
            BeautifulSoup: soup du contenue de la page
        """

        return BeautifulSoup(resp.content, 'lxml') if resp.ok else None

    def get_content_file(self, filename: str) -> dict:
        """Recupere le contenue d'un fichier 

        Args:
            filename (str): nom du fichier 

        Returns:
           dict: data
        """

        with open(filename) as f:
            return json.load(f)
