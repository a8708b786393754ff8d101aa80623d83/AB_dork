from .controller_base import ControllerBase


class ControllerGoogle(ControllerBase):
    """Classe controller du moteur de recherche google.

    Args:
        ControllerBase (object): controller de base 
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