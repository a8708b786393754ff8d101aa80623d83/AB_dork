from abc import ABC
from abc import abstractmethod


class ModelDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def blocks_request(self) -> bool: pass
    
    @abstractmethod
    def get_user_agent(self) -> str: pass
    
    @abstractmethod
    def get_link_search(self) -> str: pass

    @abstractmethod
    def get_link(self, a: str) -> str: pass

    @abstractmethod
    def get_title(self, h2: str) -> str: pass

    @abstractmethod
    def get_all(self, soup) -> list: pass
