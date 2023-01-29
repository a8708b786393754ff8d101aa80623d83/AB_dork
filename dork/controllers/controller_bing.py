from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerBing(ControllerBase, ControllerDork):
    """Classe controller du moteur de recherche bing. 

    Args:
        ControllerBase (object): controller de base
        ControllerDork (object): controller des dork
    """

    def __init__(self, model, view) -> None:
        """Methode constrcutrice.

        Args:
            model (object): Model du controller
            view (object): View du controller 
        """

        super().__init__(model, view)
        self.navigator = 'bingbot'
        self.search_engine = 'bing'

        self.set_url()
        self.set_user_agent()

    def set_page_count(self, page: int) -> None:
        """Ajoute le parametre pour le nombre de page. 

        Args:
            page (int): numero de page a afficher 
        """

        if page == 1:
            self.set_params({'first': 1, 'FORM': 'PERE'})
        elif page == 2:
            self.set_params({'first': int(f'{page-1}1'), 'FORM': 'PERE'})
        else:
            self.set_params(
                {'first': int(f'{page-1}1'), 'FORM': f'PERE{page-2}'})

    def search(self) -> None:
        """Methode de recherche, elle recupere la reponse de la requete, 
            le titre, lien grace au model.
            Elle affiche les resultats grace a la vue.
        """

        resp = self.get_resp()
        self.view.url(resp.url)

        if resp.ok:
            soup = self.model.get_soup(resp)
            node_main = self.model.get_main_node(soup)

            for li in node_main:
                try:
                    title = self.model.get_title(li)
                    link = self.model.get_link(li)

                except AttributeError:
                    pass

                else:
                    self.view.title(title)
                    self.view.link(link)

    def file_type(self, element: str) -> None:
        """Ajoute le mot clef filetype à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'filetype:"{element}"'})

    def in_text(self, element: str) -> None:
        """Ajoute le mot clef intext à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'intext:"{element}"'})

    def in_all_text(self, element: str) -> None:
        """Ajoute le mot clef inalltext à l'attribut params

        Args:
            element (str): element de recherche du dork
        """

        self.set_params({'q': f'inalltext:"{element}"'})

    def extension(self) -> None: pass
