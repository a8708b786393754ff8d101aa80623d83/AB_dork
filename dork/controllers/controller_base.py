import requests
from bs4 import BeautifulSoup


class ControllerBase(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.params = {}

    def requests_uri(self) -> requests.Response:
        """Effectue les requetes avec les parametres donner.

        Returns:
            requests.Response: reponse de la requete
        """

        return requests.get(self.url_base, params=self.params)