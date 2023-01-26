from abc import ABC
from abc import abstractmethod


class ControllerDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def set_item(self, item: str) -> None:  pass 

    @abstractmethod
    def set_user_agent(self) -> None: pass

    @abstractmethod
    def set_url(self) -> None: pass

    @abstractmethod
    def file_type(self, element: str) -> None: pass

    @abstractmethod
    def extension(self, element: str) -> None: pass

    @abstractmethod
    def in_text(self, element: str) -> None: pass

    @abstractmethod
    def in_all_text(self, element: str) -> None: pass
