from abc import ABC, abstractmethod


class ViewDork(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def url(self, url: str) -> None: pass

    @abstractmethod
    def title(self, title: str) -> None: pass

    @abstractmethod
    def link(self, link: str) -> None: pass

    @abstractmethod
    def user_agent(self, user_agent: str) -> None: pass
