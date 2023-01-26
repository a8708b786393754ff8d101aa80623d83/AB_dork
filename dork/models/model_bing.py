from .model_base import ModelBase
from .model_dork import ModelDork

import bs4 

class ModelBing(ModelBase, ModelDork):
    def __init__(self) -> None:
        super().__init__()
        self.navigator = 'bingbot'
        self.search_engine = 'bing'

    def blocks_request(self) -> bool: pass

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
        return data[self.navigator]

    def get_link(self, div: bs4.element.Tag) -> str:
        return div.h2.a['href']

    def get_title(self, div: bs4.element.Tag) -> str:
        return div.h2.a.text

    def get_all(self, soup: bs4.BeautifulSoup) -> list:
        return super().get_all(soup)