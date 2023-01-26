from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerGoogle(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)

        self.headers['Referer'] = 'https://www.google.com/'
        self.headers['Authority'] = 'www.google.com'

        self.set_user_agent()
        self.set_url()

        self.view.user_agent(self.user_agent)

    def set_params(self):
        """Ajoute les parametre à l'attribut params qui seront utilisée dans la requete."""

        self.params['source'] = 'lnms'
        self.params['tbm'] = 'nws'

    def set_user_agent(self) -> None:
        """Ajoute un user_agent."""

        self.user_agent = self.model.get_user_agent()
        self.headers['User-agent'] = self.user_agent

    def set_url(self) -> None:
        """Ajoute l'url on recuperer le lien de google."""

        self.url = self.model.get_link_search()

    def file_type(self, element: str):
        """Effectue une requete avec le mot clef filetype

        Args:
            element (str): element entrez par l'utilisateur pour la recherche
        """

        self.params['q'] = f'"{element}"'
        self.set_params()
        resp = self.get_resp()
        if resp.ok:
            print(resp.url)
            print(resp.request.headers)  # FIXME regler ca

    def extension(self): pass

    def in_text(self): pass

    def in_all_text(self): pass
