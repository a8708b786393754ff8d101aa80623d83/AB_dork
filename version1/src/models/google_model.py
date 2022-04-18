import json
from pathlib import Path

from .model_base import ModelBase

class ModelGoogleDork(ModelBase):
    """Méthode constructrice, herite des attributs de l'objet ModelBase."""
    
    NAME_FILE_SAVING_ITEMS_GOOGLE_DORK = 'items_google_dork.json'
    NAME_FILE_SAVING_CREDENTIALS = 'api_information.json'
    def __init__(self):
        super().__init__()
        
    def get_creditial(self): 
        """Recupere toutes les informations api dans un fichier JSON

        Returns:
            dict|False: un dictionnaire si il y a du contenue, faux si il n'existse pas ou qu'il est vide
        """
        file = Path(self.PATH_DATA+self.NAME_FILE_SAVING_CREDENTIALS)
        if file.exists(): 
            content = file.read_text()
            if content != '': 
                return json.loads(content)
        return False

    def get_api_creditial(self): 
        """_summary_

        Returns:
            dict|False: des données si il y a du contenue, faux si il n'existse pas ou qu'il est vide
        """
        
        api_key = self.get_creditial()
        return api_key.get('api_keys') if not api_key is False else False 

    def get_cse_creditail(self): 
        """_summary_

        Returns:
            dict|False: des données si il y a du contenue, faux si il n'existse pas ou qu'il est vide
        """
        
        cse = self.get_creditial()
        return cse.get('cse_id') if not cse is False else False 
    
    def get_ini_creditial(self): 
        """_summary_

        Returns:
            dict|False: des données si il y a du contenue, faux si il n'existse pas ou qu'il est vide
        """
        
        init = self.get_creditial()
        return init.get('init_creditials') if not init is False else False 

        
    def set_creditials(self, data: dict): 
        """Ecrit les informations de l'api, cette methode sera utiliser dans les methode de pivot

        Args:
            data (dict): donnée a ecrire
        """
        
        with open(self.PATH_DATA+self.NAME_FILE_SAVING_CREDENTIALS, 'w') as f: 
            json.dump(data, f) 
            
    def get_number_keys_api(self): 
        """Donne le nombre d'identifiant stockée 

        Returns:
            int|False: nombre de 
        """
        content = self.get_api_creditial()

        if content: 
            return len(content)
        return False 