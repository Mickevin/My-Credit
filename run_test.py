import unittest
from fastapi.testclient import TestClient
from run import square_, app

class TestAPI(unittest.TestCase): # Test de l'API
    client = TestClient(app)
    data = {'n' : 5}

    # Test de la réponse de l'API
    def test_response_api(self):
        reponse = self.client.post('/square', json=self.data)
        self.assertEqual(reponse.status_code, 200)

    # Test du type de la réponse de l'API
    def test_type_response_api(self):
        reponse = self.client.post('/square', json=self.data)
        self.assertEqual(dict, type(reponse.json()))
    


# Test de la fonction square_
class Test_functions(unittest.TestCase):
    def test_return(self):
        self.assertEqual(square_(5), 25)
        self.assertEqual(square_(10), 100)
        self.assertEqual(square_(0), 0)
        self.assertEqual(square_(-5), 25)

    def test_type(self):
        self.assertEqual(type(square_(5)), int)

    def test_input_type(self):
        self.assertEqual(square_('-5'), 'Please enter a number')
