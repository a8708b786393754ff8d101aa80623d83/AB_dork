from .controller_base import ControllerBase
from .controller_dork import ControllerDork

class ControllerGoogle(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'google'

        self.set_user_agent()
        self.set_url()


    def set_user_agent(self) -> None:
        """Ajoute un user_agent."""

        self.user_agent = self.model.get_user_agent()


    def set_url(self) -> None:
        """Ajoute l'url on recuperer le lien de google."""

        self.url = self.model.get_link_search()


    def file_type(self, element: str): 
        """Effectue une requete avec le mot clef filetype

        Args:
            element (str): element entrez par l'utilisateur pour la recherche
        """

        self.params['q'] = f'filetype: "{element}"' 
        print(self.user_agent)
        resp = self.get_resp()
        
        if resp.ok: 
            print(resp.text) #FIXME regler ca
            
    def extension(self): 
        pass 

    def in_text(self): pass

    def in_all_text(self): pass
