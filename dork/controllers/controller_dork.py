from abc import ABC
from abc import abstractmethod


class ControllerDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def set_user_agent() -> None: pass

    @abstractmethod
    def set_url() -> None: pass

    @abstractmethod
    def file_type(self): pass

    @abstractmethod
    def extension(self): pass

    @abstractmethod
    def in_text(self): pass

    @abstractmethod
    def in_all_text(self): pass
