import json

from pathlib import Path


class ModelBase:
    """Classe qui s'occupe des donner en genérale."""  # FIXME recercie le docstring

    PATH_DATA = 'data/'
    NAME_FILE_EXTENSION = 'extension.json'

    def __init__(self):
        self.number_cutt = 150

    def write_json_dict(self, filename: str, data: dict):
        """Ecris les donnes en format JSON dans un fichier JSON.

        Args:
            filename (str): seulement le nom du fichier
            data (dict): dictionnaire de donnée a écrire
        """

        with open(self.PATH_DATA+filename, 'w') as f:
            json.dump(data, f)

    def cutt_list(self, filename: str, filename_ouput: str):
        """Coupe le fichier en pars, tout en gardant l'originale, on laisse le choix a l'utilisateur ou il peut stocker la sortit.

        Args:
            filename (str): seulement nom du fichier
            filename_ouput (str): nom du fichier/ chemin relatife
        """

        with open(self.PATH_DATA+filename, 'r') as f:
            with open(filename_ouput, 'w') as f_two:

                for line in f.readlines()[:self.number_cutt]:
                    if line != '':
                        f_two.write(f'{line}')

    def get_extension(self):
        """Cherche le fichier d'extensions est donne le resultat, cette methode seras/dois utiliser que si le fichier existse.

        Args:
            filename (str): nom du fichier (non le chemin relative)

        Returns:
            dict : donner du fichier 
        """

        with open(self.PATH_DATA+self.NAME_FILE_EXTENSION) as f:
            return json.loads(f.read())

    def is_save(self, filename: str):
        """Methode qui regarde si le fichier existse.

        Args:
            filename (str): nom du fichier

        Returns:
            bool: True si le fichier existe est qu'il y a du contenue, sinon False
        """

        file = Path(self.PATH_DATA+filename)
        if file.exists():
            if file.read_text() != '':
                return True
        return False
