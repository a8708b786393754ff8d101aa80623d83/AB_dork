#! /usr/local/bin/python3.10
import sys
import unittest

sys.path.append('../../src/')
from models.google_model import ModelGoogleDork


class TestGoogleDorkModel(unittest.TestCase):
    def setUp(self):
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
