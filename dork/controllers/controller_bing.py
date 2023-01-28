from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerBing(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'bingbot'

        self.set_url()
        self.set_user_agent()

        self.view.user_agent(self.user_agent)

    def set_page_count(self, page: int):
        if page == 1:
            self.set_params({'first': 1, 'FORM': 'PERE'})
        elif page == 2:
            self.set_params({'first': int(f'{page}1'), 'FORM': 'PERE'})
        else:
            self.set_params({'first': int(f'{page}1'), 'FORM': f'PERE{page-2}'})

    def search(self) -> None:
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

    def file_type(self, element: str) -> None:
        self.set_params({'q': f'filetype:"{element}"'})

    def in_text(self, element: str) -> None:
        self.set_params({'q': f'intext:"{element}"'})

    def in_all_text(self, element: str) -> None:
        self.set_params({'q': f'inalltext:"{element}"'})

    def extension(self): pass
