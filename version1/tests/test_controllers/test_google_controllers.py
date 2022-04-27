#! /usr/local/bin/python3.10
import sys
import unittest

sys.path.append('../../src/')
from controllers.google_controller import GoogleDorkController
from models.google_model import ModelGoogleDork
from views.view import ViewGoogleDork


class TestGoogleDorkController(unittest.TestCase): 
    
    
    def setUp(self):
        self.controller = GoogleDorkController(ModelGoogleDork(), ViewGoogleDork())
    
    def test_pivote(self): 
        self.controller.model.PATH_DATA = '../../test_model/'
        self.controller.model.NAME_FILE_SAVING_CREDENTIALS = 'api_information_test.json'

        for i in range(0, 10000): 
            self.assertIsNone(self.controller.pivote_credentials())
            
             



if __name__ == '__main__':
    unittest.main()