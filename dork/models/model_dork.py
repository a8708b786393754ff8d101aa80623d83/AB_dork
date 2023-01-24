from abc import ABC
from abc import abstractmethod


class ModelDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_link(self) -> str: pass

    @abstractmethod
    def get_link_search(self) -> str: pass

    @abstractmethod
    def get_title(self) -> str: pass

    @abstractmethod
    def get_all(self) -> list: pass

    @abstractmethod
    def get_user_agent(self) -> str: pass

    @abstractmethod
    def get_url(self) -> str: pass
