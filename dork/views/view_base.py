from colorama import Fore
from colorama import Back


class ViewBase(object):
    """Classe de vue de base

    Args:
        object (_type_): objet
    """

    def __init__(self) -> None:
        """Methode constructrice."""

        self.fore = Fore
        self.back = Back

    def banner(self) -> None:
        """Affichage de la banniere."""

        print(f"""
             █████  ██████          ██████   ██████  ██████  ██   ██ 
            ██   ██ ██   ██         ██   ██ ██    ██ ██   ██ ██  ██  
            ███████ ██████          ██   ██ ██    ██ ██████  █████   
            ██   ██ ██   ██         ██   ██ ██    ██ ██   ██ ██  ██  
            ██   ██ ██████  ███████ ██████   ██████  ██   ██ ██   ██  since 2023
                                                         
        """)

    def query(self, query: str) -> None:
        """Affiche la requete 

        Args:
            query (str): requete 
        """

        print(self.back.LIGHTRED_EX + self.fore.WHITE +
              f'Query: {query}' + self.fore.RESET + self.back.RESET)
