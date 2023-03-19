import yaml


class ModelExtensionYaml:
    """Classe d'extension pour la manipulation de donnée YAML."""

    @classmethod
    def get_content_file(cls, filename: str) -> dict:
        """Recupere le contenue d'un fichier yaml

        Args:
            filename (str): nom du fichier

        Returns:
            dict: contenue du fichier 
        """

        with open(filename) as f:
            return yaml.safe_load(f)
