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
        self.url = ''
        self.user_agent = ''
        self.params = {}
        self.headers = {'User-agent': '',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1'}

    def get_resp(self) -> requests.Response:
        """Effectue une requetes en donnent les parametre est les user agent.

        Returns:
            requests.Response: reponse de la requete
        """

        return requests.get(self.url, params=self.params, headers=self.headers, verify=True)
