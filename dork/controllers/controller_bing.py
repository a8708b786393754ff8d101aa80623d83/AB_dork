from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerBing(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'bingbot'

        self.set_url()
        self.set_user_agent()

    def set_user_agent(self) -> None:
        """Ajoute un user agent."""

        self.user_agent = self.model.get_user_agent()
        self.headers['User-agent'] = self.user_agent

    def set_url(self) -> None:
        """Ajoute l'url on recuperer le lien de google."""

        self.url = self.model.get_link_search()

    def file_type(self, element: str) -> None:
        if self.params.get('q'):
            self.params['q'] += f' filetype:"{element}"'
        else:
            self.params['q'] = f' filetype:"{element}"'

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
        if self.params.get('q'):
            self.params['q'] += f' intext:"{element}"'
        else:
            self.params['q'] = f'intext:"{element}"'

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
        if self.params.get('q'):
            self.params['q'] += f' inalltext:"{element}"'
        else:
            self.params['q'] = f'inalltext:"{element}"'

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
