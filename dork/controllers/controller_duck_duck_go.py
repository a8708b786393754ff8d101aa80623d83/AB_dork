from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import dork.utils as utils
from .controller_base import ControllerBase


class ControllerDuckDuckGo(ControllerBase):
    """Classe controller du moteur de recherche duck duck go. 

    Args:
        ControllerBase (object): controller de base
    """

    def __init__(self, model, view) -> None:
        """Methode constrcutrice.

        Args:
            model (object): Model du controller
            view (object): View du controller 
        """

        super().__init__(model, view)

    def get_soup(self, resp: requests.Response) -> BeautifulSoup:
        """Recupere le soup d'une page html

        Args:
            resp (requests.Response): reponse de la requete

        Returns:
            BeautifulSoup: soup du contenue de la page
        """

        return BeautifulSoup(resp.html.html, 'lxml') if resp.ok else None

    def get_resp(self, proxy: bool = False):
        """_summary_

        Args:
            proxy (bool, optional): _description_. Defaults to False.

        Returns:
            requests.Response: _description_
        """

        s = HTMLSession()

        if proxy:
            proxy = utils.get_proxy()

        return s.get(self.url, params=self.params, headers=self.headers, verify=True, proxies=proxy)

    def search(self, page: int = 0) -> None:
        resp = self.get_resp()
        resp.html.render()

        self.view.url(resp.url)

        if resp.ok:
            soup = self.model.get_soup(resp)
            node_main = self.model.get_main_node(soup)
