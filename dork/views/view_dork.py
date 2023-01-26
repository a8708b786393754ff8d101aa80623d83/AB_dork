from abc import ABC, abstractmethod

class ViewDork(ABC): 
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def title(self, title: str): pass 

    @abstractmethod
    def link(self, link: str): pass 

    @abstractmethod
    def user_agent(self, user_agent: str): pass 


