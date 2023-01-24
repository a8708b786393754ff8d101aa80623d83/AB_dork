from .model_base import ModelBase
from .model_dork import ModelDork

import random

class ModelGoogle(ModelBase, ModelDork):
    def __init__(self):
        super().__init__()

    def get_link_search(self) -> str: 
        """Recupere le lien de recherche de google

        Returns:
            str: lien de recherche de google
        """

        data = self.get_content_file(self.const.PATH_DATA + self.const.FILENAME_LINKS)
        return data['google']
    
    def get_user_agent(self) -> str: 
        """Recupere un user agent 

        Returns:
            str: user agent
        """

        data = self.get_content_file(self.const.PATH_DATA + self.const.FILENAME_USER_AGENT)
        return data['chrome'][random.randint(0, len(data['chrome']))]

    def get_title(self) -> str: pass

    def get_all(self) -> list: pass
