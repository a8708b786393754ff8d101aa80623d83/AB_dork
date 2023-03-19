from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerGoogle(ControllerBase, ControllerDork):
    """Classe controller du moteur de recherche google.

    Args:
        ControllerBase (object): controller de base 
        ControllerDork (object): controller des dork
    """

    def __init__(self, model, view) -> None:
        """Methode constructrice.

        Args:
            model (object): Model du controller
            view (object): View du controller
        """

        super().__init__(model, view)

        self.headers['Referer'] = 'https://www.google.com/'
        self.headers['Authority'] = 'www.google.com'

    def search(self) -> None:
        """Methode de recherche."""

        pass

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

    def extension(self, element: str) -> None:
        """Ajoute le mot clef extension à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'ext:"{element}"'})

    def map(self, element: str) -> None:
        """Ajoute le mot clef map a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'map:"{element}"'})

    def film(self, element: str) -> None:
        """Ajoute le mot clef film a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'film:"{element}"'})

    def in_anchor(self, element: str) -> None:
        """Ajoute le mot clef inanchor a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'inanchor:"{element}"'})

    def blog_url(self, element: str) -> None:
        """Ajoute le mot clef blogurl a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'blogurl:"{element}"'})

    def loc(self, element: str) -> None:
        """Ajoute le mot clef loc a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'loc:"{element}"'})

    def site(self, element: str) -> None:
        """Ajoute le mot clef site a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'site:"{element}"'})
