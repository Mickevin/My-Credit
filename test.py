import unittest

import unittest
from fastapi.testclient import TestClient
from app import app, users_db

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    
    def test_create_user(self):
        # Test de la création d'un utilisateur
        user_data = {"username": "john_doe", "email": "john@example.com"}
        response = self.client.post("/users/", json=user_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), user_data)
    
    def test_get_user(self):
        # Test de la récupération d'un utilisateur existant
        user_data = {"username": "jane_doe", "email": "jane@example.com"}
        users_db.append(user_data)
        
        response = self.client.get("/users/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), user_data)
    
    def test_get_user_not_found(self):
        # Test de la récupération d'un utilisateur inexistant
        response = self.client.get("/users/99")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"error": "User not found"})

if __name__ == '__main__':
    unittest.main()