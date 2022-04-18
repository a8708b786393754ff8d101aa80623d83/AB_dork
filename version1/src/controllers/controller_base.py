class ControllerBase:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def already_registered(self, filename: str):
        """_summary_ FIXME

        Args:
            filename (str): _description_

        Returns:
            _type_: _description_
        """

        return self.model.is_save(filename)
