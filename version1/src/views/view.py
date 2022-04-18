from colorama import Fore


class ViewBase:
    def save_file(self, name_file: str):
        print(Fore.MAGENTA+'[*] Fichier '+name_file+' sauvegarder'+Fore.RESET)


class ViewPick(ViewBase):
    def __init__(self):
        super().__init__()
        self.choice = 0

    def choice_mode(self):
        print("""
            Mode 1: email:password
            Mode 2: email       
        """)
        self.choice = input(
            'Veuillez choisir un mode: ')  # FIXME verifier si c'est un nombre


class ViewGoogleDork(ViewBase):
    def __init__(self):
        super().__init__()

    def update_file(self, name_file: str): 
        print(Fore.MAGENTA+'[*] Fichier '+name_file+' mis a jour '+Fore.RESET)
        
    def start(self):
        print(Fore.GREEN+'[+] Enregistrement des liens'+Fore.RESET)

    def pivot(self):
        print(Fore.GREEN+'[+] Les identifiant on pivoter'+Fore.RESET)


class ViewScraping(ViewBase):
    def __init__(self):
        super().__init__()

    def start(self):
        print(Fore.GREEN+'[+] Enregistrement des extensions'+Fore.RESET)
