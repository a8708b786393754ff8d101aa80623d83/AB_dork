from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerGoogle(ControllerBase, ControllerDork):
    """Classe controller du moteur de recherche google.

    Args:
        ControllerBase (object): controller de base 
        ControllerDork (object): controller des dork
    """

    def __init__(self, model, view)->None:
        """Methode constructrice.

        Args:
            model (object): Model du controller
            view (object): View du controller
        """

        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'google'

        self.headers['Referer'] = 'https://www.google.com/'
        self.headers['Authority'] = 'www.google.com'

        self.set_user_agent()
        self.set_url()

    def search(self) -> None:
        """Methode de recherche."""

        pass 
    

    def file_type(self, element: str)->None:
        """Ajoute le mot clef filetype à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'filetype:"{element}" '})

    def extension(self, element: str)->None: 
        """Ajoute le mot clef extension à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'extension:"{element}" '})


    def in_text(self, element: str)->None: 
        """Ajoute le mot clef intext à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'intext:"{element}" '})



    def in_all_text(self, element: str)->None: 
        """Ajoute le mot clef inallatext à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'inalltext:"{element}" '})

