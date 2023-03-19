import json


class ModelExtensionJson:
    """Classe d'extension pour la manipulation de donnée JSON."""

    @classmethod
    def get_content_file(cls, filename: str) -> dict:
        """Recupere le contenue d'un fichier 

        Args:
            filename (str): nom du fichier 

        Returns:
           dict: data
        """

        with open(filename) as f:
            return json.load(f)
