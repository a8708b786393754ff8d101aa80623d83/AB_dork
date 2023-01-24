from .model_base import ModelBase
from .model_dork import ModelDork


class ModelGoogle(ModelBase, ModelDork):
    def __init__(self):
        super().__init__()

    def get_link(self) -> str: pass

    def get_title(self) -> str: pass

    def get_all(self) -> list: pass

    def get_link_search(self) -> str: pass
