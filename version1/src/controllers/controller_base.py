import requests 
import re 
class ControllerBase:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.url_base: str

    def already_registered(self, filename: str):
        """_summary_ FIXME

        Args:
            filename (str): _description_

        Returns:
            _type_: _description_
        """

        return self.model.is_save(filename)

    
    def requests_uri(self, params: dict):
        """Effectue les requetes avec les parametres donner.

        Args:
            params (dict): parametre pour ajouter a l'url

        Returns:
            requests.Response: reponse de la requete
        """

        return requests.get(self.url_base, params=params)
    
    def is_link(self, element: str):
        """Verifie si c'est bien une url garce au expression reguliere

        Args:
            element (str): element a verifier

        Returns:
            bool: vrai si c'est un bien un url, sinon false
        """
        
        return re.search('^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$', element)