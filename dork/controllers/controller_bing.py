from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerBing(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'bingbot'

    def set_user_agent(self) -> None:
        """Ajoute un user_agent."""

        self.user_agent = self.model.get_user_agent()
        self.headers['User-agent'] = self.user_agent

    def set_url(self) -> None:
        """Ajoute l'url on recuperer le lien de google."""

        self.url = self.model.get_link_search()

    def file_type(self): pass

    def extension(self): pass

    def in_text(self): pass

    def in_all_text(self): pass
