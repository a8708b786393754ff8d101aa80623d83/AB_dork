from abc import ABC, abstractmethod


class ViewDork(ABC):
    """View des dork, c'est une classe abstraicte

    Args:
        ABC (object): class mere abs
    """

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def url(self, url: str) -> None: ...

    @abstractmethod
    def title(self, title: str) -> None: ...

    @abstractmethod
    def link(self, link: str) -> None: ...

    @abstractmethod
    def user_agent(self, user_agent: str) -> None: ...
