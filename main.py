#! /usr/local/bin/python3.10
import time

from dork.controllers.google_controller import GoogleDorkController
from dork.controllers.scraping_controller import ScrapingController

from dork.models.google_model import ModelGoogleDork
from dork.models.srcaping_model import ScrapingModel

from dork.views.view import ViewGoogleDork, ViewScraping

start = time.perf_counter()

extension_suffixe = {
                    '(bdd|base de donée|database) ': 'https://www.file-extension.info/fr/fichiers-de-base-de-donnes/',
                    '(system|windows|linux|javaOs|os)': 'https://www.file-extension.info/fr/fichiers-systme',
                    '(compresse|compress|compresser|zip)': 'https://www.file-extension.info/fr/fichiers-compresss',
                    '(texte|txt|text|script|file)': 'https://www.file-extension.info/text-files'
                    }

scrap = ScrapingController(ScrapingModel(), ViewScraping())
google_dork_obj = GoogleDorkController(ModelGoogleDork(), ViewGoogleDork())

if not scrap.already_registered(ScrapingModel.NAME_FILE_EXTENSION):  
    scrap.save_suffix_extension(extension_suffixe)
    
if not google_dork_obj.already_registered(ModelGoogleDork.NAME_FILE_SAVING_ITEMS_GOOGLE_DORK): 
    google_dork_obj.file_type()

    
print(time.perf_counter() - start) 
