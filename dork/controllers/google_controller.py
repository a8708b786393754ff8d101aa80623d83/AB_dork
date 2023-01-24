import requests
import urllib3

from .controller_base import ControllerBase
# NOTE desactive le message d'attention ( comme on a mis a false a la verification de certification)
urllib3.disable_warnings()


class GoogleDorkController(ControllerBase):
    """Methode constructrice, elle a besoin d'un model, elle instancie les variable pour la clef d'api rest de google, l'id de la CSE, la base de l'url

        Args:
            model_obj (object): object model
    """

    def __init__(self, model_obj, view_obj):
        super().__init__(model_obj, view_obj)
        
    def file_type(self): pass 

    