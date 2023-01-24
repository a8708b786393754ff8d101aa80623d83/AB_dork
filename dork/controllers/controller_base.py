import requests


class ControllerBase(object):
    """Classe de base des controller

    La méthode constructrice initialise des attributs est initailise deux object, le model est la vue

    Args:
        model (object): objet model
        view (object): objet view

    """

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.url: str
        self.navigator: str
        self.search_engine: str
        self.user_agent: str
        self.params: dict

    def get_resp(self) -> requests.Response:
        """Effectue une requetes en donnent les parametre est les user agent.

        Returns:
            requests.Response: reponse de la requete
        """

        return requests.get(self.url, params=self.params, headers={'User-agent': self.user_agent})
