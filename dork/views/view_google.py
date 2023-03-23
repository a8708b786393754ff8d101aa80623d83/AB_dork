from .view_base import ViewBase
from .view_dork import ViewDork


class ViewGoogle(ViewBase, ViewDork):
    """Classe View de l'affichage de recherche google. 

    Args:
        ViewBase (object): view de base
        ViewDork (object): view des dork
    """

    def __init__(self) -> None:
        """Méthode constructrice."""

        super().__init__()

    def title(self, title: str) -> None:
        """Affiche un titre

        Args:
            title (str): titre
        """

        print(self.fore.RED + f'[+*+]Title: {title}' + self.fore.RESET)

    def link(self, link: str) -> None:
        """Afficfhe un lien

        Args:
            link (str): lien
        """

        print(self.fore.CYAN + f'[/-\]Link: {link}' + self.fore.RESET)

    def user_agent(self, user_agent: str) -> None:
        """Afficfhe un user agent

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

    def url_blocked(self) -> None: 
        """Affiche un message qui dit que google est bloqué a cause du captchat."""
        
        print(self.back.WHITE + self.fore.RED + 'Google blocked (captchat)!' + self.back.RESET + self.fore.RESET)