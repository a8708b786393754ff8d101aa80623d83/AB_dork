import requests
from bs4 import BeautifulSoup


class ControllerBase(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def already_registered(self, filename: str):
        """_summary_ #FIXME

        Args:
            filename (str): _description_

        Returns:
            _type_: _description_
        """

        return self.model.is_save(filename)

    def requests_uri(self, params: dict) -> requests.Response:
        """Effectue les requetes avec les parametres donner.

        Args:
            params (dict): parametre pour ajouter a l'url

        Returns:
            requests.Response: reponse de la requete
        """

        return requests.get(self.url_base, params=params)

    def get_soup(text: str) -> BeautifulSoup:
        """Renvoie le soup d'une page html

        Args:
            text (str): texte de la reponse de la requete

        Returns:
            BeautifulSoup: soup
        """

        return BeautifulSoup(text, 'lxml')
