from .model_base import ModelBase
from .model_dork import ModelDork


class ModelBing(ModelBase, ModelDork):
    def __init__(self) -> None:
        super().__init__()

    def blocks_request(self) -> bool: pass

    def get_link(self) -> str: pass

    def get_link_search(self) -> str: pass

    def get_title(self) -> str: pass

    def get_all(self) -> list: pass

    def get_user_agent(self) -> str: pass
