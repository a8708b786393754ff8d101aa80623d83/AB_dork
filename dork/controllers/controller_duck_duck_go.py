from .controller_base import ControllerBase


class ControllerDuckDuckGo(ControllerBase):
    """Classe controller du moteur de recherche duck duck go. 

    Args:
        ControllerBase (object): controller de base
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
