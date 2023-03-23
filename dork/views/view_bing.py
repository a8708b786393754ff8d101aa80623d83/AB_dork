from .view_base import ViewBase
from .view_dork import ViewDork


class ViewBing(ViewBase, ViewDork):
    """Classe View de l'affichage de recherche bing. 

    Args:
        ViewBase (object): view de base
        ViewDork (object): view des dork
    """

    def __init__(self) -> None:
        """Méthode constructrice."""

        super().__init__()

    def title(self, title: str) -> None:
        """Affiche le titre

        Args:
            title (str): titre
        """

        print(self.fore.RED + f'[+*+]Title: {title}' + self.fore.RESET)

    def link(self, link: str) -> None:
        """Affiche un lien

        Args:
            link (str): lien
        """

        print(self.fore.CYAN + f'[/-\]Link: {link}' + self.fore.RESET)

    def user_agent(self, user_agent: str) -> None:
        """Affiche l'user agent 

        Args:
            user_agent (str): user agent 
        """

        print(self.fore.GREEN +
              f'[*-*]User agent: {user_agent}' + self.fore.RESET)

    def url(self, url: str) -> None:
        """Affiche l'url de la requete

        Args:
            url (str): url
        """

        print(self.fore.YELLOW + f'[+*-*+]Url: {url} ' + self.fore.RESET)

    def none_result(self) -> None:
        """Affiche une message quand ya pas de resultat."""

        print(self.fore.MAGENTA + 'Aucun resultas de la recherche' + self.fore.RESET)
        exit(0)