#! /usr/local/bin/python3.10
import time

from src.controllers.google_controller import GoogleDorkController
from src.controllers.scraping_controller import ScrapingController
from src.controllers.bing_controller import BingDorkController

from src.models.google_model import ModelGoogleDork
from src.models.bing_model import ModelBingDork
from src.models.srcaping_model import ScrapingModel

from src.views.view import ViewGoogleDork, ViewScraping

start = time.perf_counter()

extension_suffixe = {
                    'intext: (bdd OR base de donée OR database) ': 'https://www.file-extension.info/fr/fichiers-de-base-de-donnes/',
                    'intext: (system OR windows OR linuxjavaOs OR os)': 'https://www.file-extension.info/fr/fichiers-systme',
                    'intext: (compresse OR compress OR compresser OR zip)': 'https://www.file-extension.info/fr/fichiers-compresss',
                    'intext: (texte OR txt OR text OR script OR file)': 'https://www.file-extension.info/text-files'
                    }

scrap = ScrapingController(ScrapingModel(), ViewScraping())
google_dork_obj = GoogleDorkController(ModelGoogleDork(), ViewGoogleDork())
bing_obj = BingDorkController(ModelBingDork(), ViewGoogleDork())

if not scrap.already_registered(ScrapingModel.NAME_FILE_EXTENSION):  
    scrap.save_suffix_extension(extension_suffixe)


if not bing_obj.already_registered(ModelBingDork.NAME_FILE_SAVING_ITEMS_BING_DORK):
    bing_obj.file_type()
    # bing_obj.pastlib()
    
if not google_dork_obj.already_registered(ModelGoogleDork.NAME_FILE_SAVING_ITEMS_GOOGLE_DORK): 
    # google_dork_obj.file_type()
    pass 

    
print(time.perf_counter() - start) 