import requests


class ControllerBase(object):
    """Classe de base des controller

    La méthode constructrice initialise des attributs est initailise deux object, le model est la vue

    Args:
        model (object): objet model
        view (object): objet view

    """

    def __init__(self, model, view) -> None:
        """Methode constructrice

        Args:
            model (object): objet model
            view (object): objet view
        """

        self.model = model
        self.view = view
        self.query = ''
        self.url = ''
        self.item = ''
        self.user_agent = ''
        self.params = {}
        self.headers = {'User-agent': '',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1'}

    def set_item(self, item: str) -> None:
        """Ajoute un item (element de la recher).

        Args:
            item (str): element a rechercher.
        """

        self.params['q'] = self.item = self.query = f'{item} '

    def set_query(self, element: str | int) -> None:
        """Ajoute l'emement a la requete, la requete prend que les dorks,
            elle evite les parametres comme les conteur de page 
            ou autres qui n'ont rien avoir avec les requetes dork.

        Args:
            element (str): element a ajoutée.
        """

        if isinstance(element, str):
            for dork in self.model.const.DORK:
                if element.startswith(dork):
                    self.query += f'{element} '

    def set_params(self, data: dict) -> None:
        """Ajoute les parametre, 
        elle concatene la valeur de la clef si elle existe, 
        sinon elle ajoute a l'aatribut params.

        Args:
            data (dict): donnée a inserez.
        """

        for key, value in data.items():
            self.set_query(value)

            if key in self.params:
                self.params[key] += f'{value} '
            else:
                self.params[key] = value

    def set_user_agent(self) -> None:
        """Ajoute un user agent."""

        self.headers['User-agent'] = self.user_agent = self.model.get_user_agent()

    def set_url(self) -> None:
        """Ajoute l'url, on recuperer le lien du moteur de recherche."""

        self.url = self.model.get_link_search()

    def get_resp(self) -> requests.Response:
        """Effectue une requetes GET en donnent les parametre est les user agent.

        Returns:
            requests.Response: reponse de la requete
        """

        return requests.get(self.url, params=self.params, headers=self.headers, verify=True)
