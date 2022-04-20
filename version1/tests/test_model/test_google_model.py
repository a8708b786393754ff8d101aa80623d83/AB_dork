#! /usr/local/bin/python3.10
import sys
sys.path.append('../../src/')
import unittest
import faker 

from controllers.google_controller import GoogleDorkController
from models.google_model import ModelGoogleDork
from views.view import ViewGoogleDork


class TestGoogleDork(unittest.TestCase):
    def setUp(self):
        self.fake = faker.Faker('fr_FR')
        self.model = ModelGoogleDork()

    def test_get_creditial_with_content(self): 
        self.model.PATH_DATA = '../../data/'
        
        content = self.model.get_creditial()
        self.assertNotEqual(content, False)
        
    def test_get_creditial_without_content(self): 
        self.model.PATH_DATA = ''
        self.model.NAME_FILE_SAVING_CREDENTIALS = 'api_information_test.json'
        
        content = self.model.get_creditial()
        self.assertFalse(content, False)
        
if __name__ == '__main__':
    unittest.main()
