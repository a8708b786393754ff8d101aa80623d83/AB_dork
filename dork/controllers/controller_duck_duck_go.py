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

        if proxy:
            proxy = utils.get_proxy()

        return requests.get(self.url, params=self.params, headers=self.headers, verify=True, proxies=proxy, allow_redirects=True)

    def search(self, page: int = 0) -> None:
        resp = self.get_resp()

        self.view.url(resp.url)

        if resp.ok:
            soup = self.model.get_soup(resp)
            node_main = self.model.get_main_node(soup)
            sectors = self.model.get_sector_result(node_main)
#
            for sector in sectors:
                title = self.model.get_title(sector)
                link = self.model.get_link(sector)
                self.view.title(title)
                self.view.link(link)
