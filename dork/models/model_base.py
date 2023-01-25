from pathlib import Path

import requests
import random
import json
from bs4 import BeautifulSoup

import dork.const as const


class ModelBase(object):
    """Classe de base des models."""

    def __init__(self) -> None:
        self.const = const
        self.message_blocks = ''

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