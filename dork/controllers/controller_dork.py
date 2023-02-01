from abc import ABC, abstractmethod


class ControllerDork(ABC):
    """Controller des dork, c'est une classe abstraicte

    Args:
        ABC (object): class mere abs
    """

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def search(self, page: int) -> None: ...

    @abstractmethod
    def file_type(self, element: str) -> None: ...

    @abstractmethod
    def extension(self, element: str) -> None: ...

    @abstractmethod
    def in_text(self, element: str) -> None: ...

    @abstractmethod
    def in_all_text(self, element: str) -> None: ...
    
    @abstractmethod
    def map(self, element: str) -> None: ...

    @abstractmethod
    def film(self, element: str) -> None: ...

    @abstractmethod
    def in_anchor(self, element: str) -> None: ...

    @abstractmethod
    def blog_url(self, element: str) -> None: ...

    @abstractmethod
    def loc(self, element: str) -> None: ...

    @abstractmethod
    def site(self, element: str) -> None: ...


