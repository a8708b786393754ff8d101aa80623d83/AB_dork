import yaml 


class ModelExtensionYaml: 
    
    @classmethod
    def get_content_file(cls, filename: str) -> dict: 
        with open(filename) as f: 
            return yaml.safe_load(f)
        
        