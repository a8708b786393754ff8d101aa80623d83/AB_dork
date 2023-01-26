from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerBing(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'bingbot'
        self.item = ''

        self.set_url()
        self.set_user_agent()

        self.view.user_agent(self.user_agent)


    def file_type(self, element: str) -> None:
        self.set_params({'q': f'filetype:"{element}"'})
        resp = self.get_resp()
        if resp.ok:
            soup = self.model.get_soup(resp)
            for li in soup.select('main li'):
                try:
                    title = self.model.get_title(li)
                    link = self.model.get_link(li)
                except AttributeError:
                    pass
                else:
                    self.view.title(title)
                    self.view.link(link)

    def in_text(self, element: str) -> None:
        self.set_params({'q': f'intext:"{element}"'})
        resp = self.get_resp()

        if resp.ok:
            soup = self.model.get_soup(resp)
            for li in soup.select('main li'):
                try:
                    title = self.model.get_title(li)
                    link = self.model.get_link(li)
                except AttributeError:
                    pass
                else:
                    self.view.title(title)
                    self.view.link(link)

    def in_all_text(self, element: str):

        self.set_params({'q': f'inalltext:"{element}"'})
        resp = self.get_resp()
        if resp.ok:
            soup = self.model.get_soup(resp)
            for li in soup.select('main li'):
                try:
                    title = self.model.get_title(li)
                    link = self.model.get_link(li)
                except AttributeError:
                    pass
                else:
                    self.view.title(title)
                    self.view.link(link)

    def extension(self): pass
