from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerGoogle(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'google'

        self.headers['Referer'] = 'https://www.google.com/'
        self.headers['Authority'] = 'www.google.com'

        self.set_user_agent()
        self.set_url()

    def file_type(self, element: str):
        """Effectue une requete avec le mot clef filetype

        Args:
            element (str): element entrez par l'utilisateur pour la recherche
        """

        self.set_params({'q': f'filetype:"{element}" '})
        resp = self.get_resp()
        if resp.ok:
            print(resp.url)
            print(resp.request.headers)  # FIXME regler ca

    def extension(self): pass

    def in_text(self): pass

    def in_all_text(self): pass
