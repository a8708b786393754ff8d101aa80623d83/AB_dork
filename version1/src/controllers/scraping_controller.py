import requests

from bs4 import BeautifulSoup

from .controller_base import ControllerBase

class ScrapingController(ControllerBase):
    """Methode constructrice, elle a besoin d'un  model, elle l'initailise est creer un attribut hedears.

        Args:
            model_obj (object): objet model
    """
    def __init__(self, model_obj, view_obj):
        super().__init__(model_obj, view_obj)
        
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv :98.0) Gecko/20100101 Firefox/98.0",
        }

    def scrap_extension(self, url: str):
        """Capture les extension, cette methode marche que sur le site https://www.file-extension.info/fr/.
           La Méthode sears utiliser dans la methode self.save_suffix_extension().

        Args:
            url (str): lien de l'url

        Returns:
            list : liste d'extensions 
        """
        
        extension = []
        # NOTE Non verife certificat  SSL
        resp = requests.get(url, headers=self.headers, verify=False)
        if resp.ok:
            soup = BeautifulSoup(resp.text, 'lxml')
            for column in soup.find_all('td'):
                try:
                    extension.append(column.a['title'].lower()[1:])
                except TypeError:
                    pass

        return extension

    def save_suffix_extension(self, data: dict):
        """Enregistre les extension dans un fichier JSON.

        Args:
            data (dict) : donne a enregistrer, la clef contient le type
                                d'extension est la valeur l'url (qui seras remplacer)
        """
        
        new_data = {}
        for keys, ext in data.items():
            new_data[keys] = self.scrap_extension(ext)

        # NOTE ecrit les donner dans un fichier json
        self.model.write_json_dict(self.model.NAME_FILE_EXTENSION, new_data)
