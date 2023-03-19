import requests
import dork.utils as utils 

class ControllerBase:
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
        self.__utils = utils
        self.counter_page = 0
        self.query = ''
        self.url = ''
        self.item = ''
        self.user_agent = ''
        self.params = {}
        self.headers = {}

        self.set_url()
        self.set_header()
        
    def set_page_count(self, page: int) -> None:
        """Ajoute a l'attribut counter_page le nombre de page 

        Args:
            page (int): numero de page a afficher 
        """

        self.counter_page = page

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

        if isinstance(element, str):  # NOTE opere dessus que si l'element est une chaine de caractere
            for dork in self.model.operator_dork:
                if element.startswith(dork):
                    self.query += f'{element} '

    def set_params(self, data: dict, counter_page: bool=False) -> None:
        """Ajoute les parametre pour la requete, concatene si la clef existe deja.
        Si l'argument counter_page est vrai, il ajoute simplement les données 

        Args:
            data (dict): donnée a inserez.
            counter_page (bool): compteur de page
        """

        for key, value in data.items():
            if counter_page: 
                self.params[key] = value
            else: 
                
                self.set_query(value)

                if key in self.params:
                    if not isinstance(value, int): 
                        self.params[key] += f'{value} '
                else:
                    self.params[key] = f'{value} '

    def set_url(self) -> None:
        """Ajoute l'url, on recuperer le lien du moteur de recherche."""

        self.url = self.model.get_link_search()
        
    def set_header(self) -> None: 
        """_summary_"""
        
        self.headers = self.model.get_header()

    def get_resp(self, proxy: bool=False) -> requests.Response:
        """Effectue une requetes GET en donnent les parametre est les user agent.

        Returns:
            requests.Response: reponse de la requete
        """
        if proxy: 
            proxy = self.__utils.get_proxy()

        return requests.get(self.url, params=self.params, headers=self.headers, verify=True, proxies=proxy)
