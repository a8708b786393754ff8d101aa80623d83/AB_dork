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

    def is_blocked(self, url: str) -> bool:
        """Regarde si il ya le mot sorry qui dit qu'il y a un captchat

        Args:
            url (str): url 

        Returns:
            bool: y a sorry ou pas.
        """

        return 'sorry' in url

    def search(self) -> None:
        """Methode de recherche, cette methode ressemble beacoup a celle de bing."""

        cmpt = 1

        while cmpt <= self.counter_page:
            resp = self.get_resp()
            if self.is_blocked(resp.url):
                self.view.url_blocked()
                break

            else:
                self.view.url(resp.url)

            if resp.ok:
                soup = self.model.get_soup(resp)
                main_node = self.model.get_main_node(soup)

                sectors = self.model.get_sector_result(main_node)

                for sector in sectors:
                    title = self.model.get_title(sector)
                    link = self.model.get_link(sector)
                    if title:
                        self.view.title(title.text)
                    if link:
                        self.view.link(link)

            self.view.space_separator()
            cmpt += 1
