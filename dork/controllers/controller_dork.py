from abc import ABC
from abc import abstractmethod


class ControllerDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def file_type(self): pass

    @abstractmethod
    def extension(self): pass

    @abstractmethod
    def in_text(self): pass

    @abstractmethod
    def in_all_text(self): pass
