from .controller_base import ControllerBase
from .controller_dork import ControllerDork


class ControllerBing(ControllerBase, ControllerDork):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.navigator = 'chrome'
        self.search_engine = 'bingbot'

    def set_user_agent() -> None:
        pass

    def set_url() -> None: pass

    def file_type(self):
        return super().file_type()

    def extension(self):
        return super().extension()

    def in_text(self):
        return super().in_text()

    def in_all_text(self):
        return super().in_all_text()
