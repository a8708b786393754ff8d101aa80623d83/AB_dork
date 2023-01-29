from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerGoogle(ControllerBase, ControllerDork):
    def __init__(self, model, view)->None:
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'google'

        self.headers['Referer'] = 'https://www.google.com/'
        self.headers['Authority'] = 'www.google.com'

        self.set_user_agent()
        self.set_url()

    def search(self) -> None:pass 
    

    def file_type(self, element: str)->None:
        self.set_params({'q': f'filetype:"{element}" '})

    def extension(self)->None: pass

    def in_text(self)->None: pass

    def in_all_text(self)->None: pass
