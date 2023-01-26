from .model_base import ModelBase
from .model_dork import ModelDork

import random
import bs4


class ModelGoogle(ModelBase, ModelDork):
    def __init__(self):
        super().__init__()
        self.navigator = 'chrome'
        self.search_engine = 'google'

    def get_link_search(self) -> str:
        """Recupere le lien de recherche de google

        Returns:
            str: lien de recherche de google
        """

        data = self.get_content_file(
            self.const.PATH_DATA + self.const.FILENAME_LINKS)
        return data[self.search_engine]

    def get_user_agent(self) -> str:
        """Recupere un user agent 

        Returns:
            str: user agent
        """

        data = self.get_content_file(
            self.const.PATH_DATA + self.const.FILENAME_USER_AGENT)
        return data[self.navigator][random.randint(0, len(data[self.navigator])-1)]

    def blocks_request(self) -> bool: pass

    def get_link(self, div: bs4.element.Tag) -> str:
        return super().get_link(div)

    def get_title(self, div: bs4.element.Tag) -> str:
        return super().get_title(div)

    def get_all(self, soup: bs4.BeautifulSoup) -> list:
        return super().get_all(soup)
