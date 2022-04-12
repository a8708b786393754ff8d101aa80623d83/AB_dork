

class ControllerBase: 
    def __init__(self, model):
        self.model = model
    
    def already_registered(self, filename: str): 
        """_summary_ FIXME

        Args:
            filename (str): _description_

        Returns:
            _type_: _description_
        """
        
        return self.model.is_save(filename) 