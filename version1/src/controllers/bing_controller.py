from bs4 import BeautifulSoup

from .controller_base import ControllerBase

# faire un script qui fait une requete chez bing (https://www.bing.com/search?q=)


class BingDorkController(ControllerBase):

    def __init__(self, model, view):
        super().__init__(model, view)

        self.url_base = 'https://www.bing.com/search'
        self.data_saving = {}
        self.lang = 'fr'

    def file_type(self):
        extensions = self.model.get_extension()
        for keys, exts in extensions.items(): 
            self.data_saving[keys] = []
            for ext in exts:
                results = self.get_result({'q': f'{keys} ext:"{ext}" filetype:"{ext}" '})
                for result in results:
                    
                    try:
                        link = result['href']
                    except KeyError:
                        pass
                    else:
                        if self.is_link(link):
                            self.data_saving[keys].append(link)

        self.model.write_json_dict(
            self.model.NAME_FILE_SAVING_ITEMS_BING_DORK, self.data_saving)

    #NOTE utiliser l'api 
    def pastlib(self):
        data = {'site:pastebin.com intext:': ['@gmail.', '@yahoo.','@gmx.', '@outlook.']}
        for keys, emails in data.items(): 
            for email in emails: 
                result = self.get_result({'q': f'{keys}{email+self.lang}'})
                print(result)
                
        
        # FIXME stocker les donner pour les params de la requete   

    def get_result(self, data: dict):
        """Recupere tout les liens des resultats

        Args:
            data (dict): parametres de l'url

        Returns:
            list: liens 
        """

        resp = self.requests_uri(data)
        print(resp.url)
        main = BeautifulSoup(resp.text, 'lxml').find('main').find('ol')
        return [link for link in main.find_all('a')]


if __name__ == '__main__':
    b = BingDorkController('a', 'a')
    print(b.url_base)
