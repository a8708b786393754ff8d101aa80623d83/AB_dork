from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerDuckDuckGo(ControllerBase, ControllerDork):
    """Classe controller du moteur de recherche duck duck go. 

    Args:
        ControllerBase (object): controller de base
        ControllerDork (object): controller des dork
    """

    def __init__(self, model, view) -> None:
        """Methode constrcutrice.

        Args:
            model (object): Model du controller
            view (object): View du controller 
        """

        super().__init__(model, view)

    def search(self, page: int=0) -> None:
        resp = self.get_resp()
        self.view.url(resp.url)

        if resp.ok: 
            soup = self.model.get_soup(resp)
            print(soup)
            node_main = self.model.get_main_node(soup)
            


    def file_type(self, element: str) -> None:
        """Ajoute le mot clef filetype à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'filetype:"{element}"'})

    def in_text(self, element: str) -> None:
        """Ajoute le mot clef intext à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'intext:"{element}"'})

    def in_all_text(self, element: str) -> None:
        """Ajoute le mot clef inalltext à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'inalltext:"{element}"'})
        
    def extension(self) -> None: pass
