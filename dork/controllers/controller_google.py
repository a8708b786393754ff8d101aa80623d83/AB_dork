import requests
import urllib3

from .controller_base import ControllerBase
from .controller_dork import ControllerDork
# NOTE desactive le message d'attention ( comme on a mis a false a la verification de certification)
urllib3.disable_warnings()



class ControllerGoogle(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)

    def file_type(self): pass

    def extension(self): pass

    def in_text(self): pass

    def in_all_text(self): pass
