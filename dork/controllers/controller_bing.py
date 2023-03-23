from .controller_base import ControllerBase


class ControllerBing(ControllerBase):
    """Classe controller du moteur de recherche bing. 

    Args:
        ControllerBase (object): controller de base
    """

    def __init__(self, model, view) -> None:
        """Methode constrcutrice.

        Args:
            model (object): Model du controller
            view (object): View du controller 
        """

        super().__init__(model, view)

    def search(self) -> None:
        """Methode de recherche, elle recupere la reponse de la requete, 
            le titre, lien grace au model.
            Elle affiche les resultats grace a la vue.
            Tout est fait dans un boucle while.
        """
        cmpt = 1

        while cmpt <= self.counter_page:
            if cmpt == 1:
                self.set_params({'first': "1", 'FORM': 'PERE'}, True)

            elif cmpt == 2:
                self.set_params({'first': "11", 'FORM': 'PERE'}, True)

            else:
                self.set_params(
                    {'first': f'{cmpt-1}1', 'FORM': f'PERE{cmpt-2}'}, True)

            resp = self.get_resp()
            self.view.url(resp.url)

            if resp.ok:
                soup = self.model.get_soup(resp)
                node_main = self.model.get_main_node(soup)

                for li in node_main:
                    try:
                        title = self.model.get_title(li)
                        link = self.model.get_link(li)
                        if link:
                            self.view.link(link)
                        elif title.text:
                            self.view.title(title.text)
                    except AttributeError:
                        self.view.none_result()

            self.view.space_separator()
            cmpt += 1
