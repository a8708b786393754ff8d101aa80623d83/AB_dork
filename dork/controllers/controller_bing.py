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

    def set_page_count(self, page: int) -> None:
        """Ajoute a l'attribut counter_page le nombre de page 

        Args:
            page (int): numero de page a afficher 
        """

        self.counter_page = page

    def search(self) -> None:
        """Methode de recherche, elle recupere la reponse de la requete, 
            le titre, lien grace au model.
            Elle affiche les resultats grace a la vue.
            Tout est fait dans un boucle while.
        """

        while self.counter_page != 0:
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

            if self.counter_page == 1:
                self.set_params({'first': 1, 'FORM': 'PERE'})
            elif self.counter_page == 2:
                self.set_params(
                    {'first': int(f'{self.counter_page-1}1'), 'FORM': 'PERE'})
            else:
                self.set_params(
                    {'first': int(f'{self.counter_page-1}1'), 'FORM': f'PERE{self.counter_page-2}'})

            self.counter_page -= 1

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

    def extension(self, element: str) -> None: 
        
        self.set_params({'q': f'ext:"{element}"'})


    def map(self, element: str) -> None:
        """Ajoute le mot clef map a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'map:"{element}"'})

    def film(self, element: str) -> None:
        """Ajoute le mot clef film a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'film:"{element}"'})

    def in_anchor(self, element: str) -> None:
        """Ajoute le mot clef inanchor a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'inanchor:"{element}"'})

    def blog_url(self, element: str) -> None:
        """Ajoute le mot clef blogurl a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'blogurl:"{element}"'})

    def loc(self, element: str) -> None:
        """Ajoute le mot clef loc a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'loc:"{element}"'})

    def site(self, element: str) -> None:
        """Ajoute le mot clef site a l'attribut params

        Args:
            element (str): element de recherche
        """

        self.set_params({'q': f'site:"{element}"'})