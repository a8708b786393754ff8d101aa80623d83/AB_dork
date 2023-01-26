from .model_base import ModelBase
from .model_dork import ModelDork

import random
import bs4


class ModelGoogle(ModelBase, ModelDork):
    def __init__(self):
        super().__init__()
        self.navigator = 'chrome'
        self.search_engine = 'google'

    def blocks_request(self) -> bool: pass

    def get_link(self, div: bs4.element.Tag) -> str:
        return super().get_link(div)

    def get_title(self, div: bs4.element.Tag) -> str:
        return super().get_title(div)

    def get_all(self, soup: bs4.BeautifulSoup) -> list:
        return super().get_all(soup)
