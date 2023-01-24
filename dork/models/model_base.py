from pathlib import Path

import requests
import random
from bs4 import BeautifulSoup

import dork.const as const


class ModelBase(object):

    def get_soup(self, resp: requests.Response) -> BeautifulSoup | False:

        return BeautifulSoup(resp.text, 'lxml') if resp.ok else False

    def get_user_agent_random(self) -> str:
        
        with open(const.PATH_DATA+const.FILENAME_USER_AGENT) as f:
            lines = f.readlines()
        return lines[random.randint(0, len(lines)-1)]

    def is_save(self, filename: str):
        """Methode qui regarde si le fichier existse.

        Args:
            filename (str): nom du fichier

        Returns:
            bool: True si le fichier existe est qu'il y a du contenue, sinon False
        """

        file = Path(self.PATH_DATA+filename)
        if file.exists():
            if file.read_text() != '':
                return True
        return False
