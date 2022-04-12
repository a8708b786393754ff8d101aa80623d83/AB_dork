import requests
import urllib3

from .controller_base import ControllerBase
# NOTE desactive le message d'attention ( comme on a mis a false a la verification de certification)
urllib3.disable_warnings()


class GoogleDorkController(ControllerBase):
    """Methode constructrice, elle a besoin d'un model, elle instancie les variable pour la clef d'api rest de google, l'id de la CSE, la base de l'url

        Args:
            model_obj (object): object model
    """

    def __init__(self, model_obj):
        super().__init__(model_obj)

        self.pivot = 0
        self.page = 1
        # calculating start, (page=2) => (start=11), (page=3) => (start=21)
        self.start = (self.page - 1) * 10 + 1

        # ayoub AIzaSyBQggYLTLGkNwN1A2IU-ho3Blb7bKI8S4Q
        self.__api_key = 'AIzaSyDBWlnLaAzrqyMRp12_s8Mk3PIJIs1ZkGk'
        self.__search_engine_id = '3a3d04f12946b5dbf'  # ayoub 4a135df94ee0e5dad
        self.url_base = f'https://www.googleapis.com/customsearch/v1?key={self.__api_key}&cx={self.__search_engine_id}'

        self.__init_creditial()

    def __init_creditial(self):
        """Methode qui sert a mettre a jour le fichier des information de l'api est du cse de google, elle met comme la valeur true aux identifiant utiliser."""
        api = self.model.get_api_creditial()
        cse = self.model.get_cse_creditail()

        # recuperer le contenue originale, c'est celui la qui sera enregistrez
        content_original = self.model.get_creditial()

        for data_api, data_cse in zip(api, cse):
            for (key_api, value_api), (key_cse, value_cse) in zip(data_api.items(), data_cse.items()):
                # regarde si les information sont utiliser dans cette instance
                if key_api == self.__api_key and key_cse == self.__search_engine_id:
                    if not value_api and not value_cse:  # si il sont a False
                        # recupere les index des clef
                        i_api = content_original['api_keys'].index(
                            {key_api: False})
                        i_cse = content_original['cse_id'].index(
                            {key_cse: False})

                        # supprimer la liste ou est sont present
                        del content_original['api_keys'][i_api]
                        del content_original['cse_id'][i_cse]

                        # ajoute les identifiant utiliser a true
                        content_original['api_keys'].append({key_api: True})
                        content_original['cse_id'].append({key_cse: True})

                        break  # ANCHOR on deja ce qu'il faut pas besionde continuer

        self.model.set_creditials(content_original)

    def __requests_uri(self, params: dict):
        """Effectue les requetes avec les parametres donner.

        Args:
            params (dict): parametre pour ajouter a l'url

        Returns:
            requests.Response: reponse de la requete  
        """

        return requests.get(self.url_base, params=params)

    def __pivote_credentials(self):
        """Methode qui permet de pivoter d'identifiant pour l'api de google."""  # FIXME finir le
        # self.pivot += 1
        # if self.pivot >= 2:
        #     #TODO mettre une methode qui renitialise les true est false du fichier api
        #     exit('Un beug innatendu a été signaler')

        api = self.model.get_api_creditial()
        cse = self.model.get_cse_creditail()

        content_original = self.model.get_creditial()

        for data_api, data_cse in zip(api, cse):
            for (key_api, value_api), (key_cse, value_cse) in zip(data_api.items(), data_cse.items()):
                if not value_api and not value_cse:  # NOTE si il sont a True
                    # NOTE recupere les index des clef qui sont utiliser
                    i_api = content_original['api_keys'].index({key_api: True})
                    i_cse = content_original['cse_id'].index({key_cse: True})

                    print(i_api, i_cse); exit()
                    # del content_original['api_keys'][i_api]
                    # del content_original['cse_id'][i_cse]

                    # content_original['api_keys'].append({key_api: False})
                    # content_original['cse_id'].append({key_cse: False})
                    """
                    FIXME apres print le contenue original je suis rendu compte que toute les valuer ete a false,
                    il faut recuperez ceux qui sont a false au (TODO) tout debut est les repmlacer au attribut des identifiant
                    """
                    # print(content_original)

    def file_type(self):
        """Methode qui effectue une requete a l'api google pour les type de fichier est enregistre les données dans un fichier JSON."""

        data = self.model.get_extension()  # NOTE recuper les extensions
        data_result = {}  # NOTE les titres, les liens seront stockeés dedans

        for keys, exts in data.items():  # NOTE boucle sur les donnes recuperer dans le fichier
            for ext in exts:  # NOTE boucle sur la liste d'extension

                result = self.__requests_uri({  # NOTE effectue les requetes
                    'q': f'allintext: {keys} ',
                    'fileType': f'{ext}'
                })

                error = result.json().get('error')
                if not error is None:
                    self.__pivote_credentials()  # TODO finir cette methode

                items = result.json().get('items')
                if not items is None:  # NOTE si il y a un resultat ou qu'il y a pas d'erreur
                    for item in items:
                        data_result[keys] = {item['title']: item['link']}

        # NOTE enregistre les données
        self.model.write_json_dict(
            self.model.NAME_FILE_SAVING_ITEMS_GOOGLE_DORK, data_result)
