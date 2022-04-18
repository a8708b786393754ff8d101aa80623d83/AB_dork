import requests
import urllib3

from .controller_base import ControllerBase
# NOTE desactive les warning ( comme on a mis a false a la verification de certification)
urllib3.disable_warnings()


class GoogleDorkController(ControllerBase):
    """Methode constructrice, elle a besoin d'un model, elle instancie les variable pour la clef d'api rest de google, l'id de la CSE, la base de l'url

        Args:
            model_obj (object): object model
    """

    def __init__(self, model_obj, view_obj):
        super().__init__(model_obj, view_obj)
        # self.page = 1
        # calculating start, (page=2) => (start=11), (page=3) => (start=21)
        # self.start = (self.page - 1) * 10 + 1

        self.__api_key = 'AIzaSyCTX03P8xYvjf_t9ErZ7r85D-Rkd0nnltg'
        self.__search_engine_id = '328fb8378575e5642'
        self.creditial_use = []
        self.url_base = f'https://www.googleapis.com/customsearch/v1?key={self.__api_key}&cx={self.__search_engine_id}'
        self.pivot = 0
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

                        self.model.set_creditials(content_original)

                        return None

    def __requests_uri(self, params: dict):
        """Effectue les requetes avec les parametres donner.

        Args:
            params (dict): parametre pour ajouter a l'url

        Returns:
            requests.Response: reponse de la requete
        """

        return requests.get(self.url_base, params=params)

    def __pivote_credentials(self):
        """Methode qui permet de pivoter d'identifiant pour l'api de google."""

        self.pivot += 1
        if self.pivot > self.model.get_number_keys_api():
            exit(0)

        api = self.model.get_api_creditial()
        cse = self.model.get_cse_creditail()
        content_original = self.model.get_creditial()

        for data_api, data_cse in zip(api, cse):
            for key_api, key_cse in zip(data_api.keys(), data_cse.keys()):
                # NOTE c'est pour verifier si la clef d'api n'a pas deja utiliser dans cette session
                if not key_api in self.creditial_use:
                    self.creditial_use.append(key_api)
                    # condition sur les identifiant qui ne sont pas utilser
                    if key_api != self.__api_key and key_cse != self.__search_engine_id:
                        # NOTE recupere les index des clef qui sont utiliser
                        index_api_key_for_false = content_original['api_keys'].index(
                            {self.__api_key: True})
                        index_cse_id_for_false = content_original['cse_id'].index(
                            {self.__search_engine_id: True})

                        # NOTE recupere les index des clef qui ne sont pas utiliser
                        index_api_key_for_true = content_original['api_keys'].index({
                                                                                    key_api: False})
                        index_cse_id_for_true = content_original['cse_id'].index({
                                                                                 key_cse: False})

                        # NOTE met les id utiliser a False
                        content_original['api_keys'][index_api_key_for_false][self.__api_key] = False
                        content_original['cse_id'][index_cse_id_for_false][self.__search_engine_id] = False

                        # NOTE change les id est met a jour l'url
                        self.__search_engine_id = key_cse
                        self.__api_key = key_api
                        self.url_base = f'https://www.googleapis.com/customsearch/v1?key={self.__api_key}&cx={self.__search_engine_id}'

                        # NOTE met les id qui vont etre utiliser a True
                        content_original['api_keys'][index_api_key_for_true][self.__api_key] = True
                        content_original['cse_id'][index_cse_id_for_true][self.__search_engine_id] = True

                        self.model.set_creditials(content_original)
                        self.view.update_file(
                            self.model.NAME_FILE_SAVING_CREDENTIALS)
                        return None

    def file_type(self):
        """Methode qui effectue une requete a l'api google pour les type de fichier est enregistre les données dans un fichier JSON."""

        data = self.model.get_extension()  # NOTE recuper les extensions
        # NOTE les titres, les liens seront stockeés dedans
        data_result = {'': []}
        for keys, exts in data.items():  # NOTE boucle sur les donnes recuperer dans le fichier
            for ext in exts:  # NOTE boucle sur la liste d'extension
                # result = self.__requests_uri({'q': f'allintext: {keys} ', 'fileType': ext })
                # NOTE effectue les requetes
                result = self.__requests_uri(
                    {'fileType': ext, 'q': f' "{keys}" '})

                self.get_result(result, keys, data_result)  # ANCHOR tester ici

        # NOTE enregistre les données
        self.model.write_json_dict(
            self.model.NAME_FILE_SAVING_ITEMS_GOOGLE_DORK, data_result)
        self.view.save_file(self.model.NAME_FILE_SAVING_ITEMS_GOOGLE_DORK)

    def get_result(self, resp: requests.Response, keys, data: dict):
        """Methode qui est utiliser juste apres la requete api, 

        Args:
            resp (requests.Response): reponse de la requete api 
            keys (str|int): clef du dictionnaire de donnée
            data (dict): la ou seront enregistrez les donnée 
        """

        if not resp.json().get('error') is None:
            self.view.pivot()
            self.__pivote_credentials()

        items = resp.json().get('items')
        if not items is None:  # NOTE si il y a un resultat ou qu'il y a pas d'erreur
            for item in items:
                data[keys] = []
                data[keys].append({item['title']: item['link']})
        print(data)

    def __del__(self):
        """Met a jour les identifiants d'api pour qu'elle peuvent etre reutiliser par la suite ."""

        data = self.model.get_creditial()
        new_dict = {"api_keys": [], 'cse_id': [],
                    "init_creditials": data["init_creditials"]}

        for api_dict, cse_dict in zip(data['api_keys'], data['cse_id']):
            for key_api, key_cse in zip(api_dict.keys(), cse_dict.keys()):

                if key_api == data["init_creditials"][0] and key_cse == data['init_creditials'][1]:
                    # True aux indentifiant utiliser
                    new_dict["api_keys"].append({key_api: True})
                    new_dict["cse_id"].append({key_cse: True})
                else:
                    new_dict["api_keys"].append({key_api: False})
                    new_dict["cse_id"].append({key_cse: False})

        self.model.set_creditials(new_dict)
