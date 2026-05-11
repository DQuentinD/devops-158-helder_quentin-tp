import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        """Configuration avant chaque test"""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_status_code(self):
        """Test 1 : Verifier que la page repond avec un code 200 (OK)"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        print("Test 1 reussi : Code HTTP 200")

    def test_response_contains_hello(self):
        """Test 2 : Verifier que la reponse contient 'Hello'"""
        response = self.app.get('/')
        self.assertIn('Hello', response.data.decode('utf-8'))
        print("Test 2 reussi : La reponse contient 'Hello'")

    def test_response_not_empty(self):
        """Test 3 : Verifier que la reponse n'est pas vide"""
        response = self.app.get('/')
        self.assertTrue(len(response.data) > 0)
        print("Test 3 reussi : La reponse n'est pas vide")

    def test_response_type_is_string(self):
        """Test 4 : Verifier que la reponse est une chaine de caracteres"""
        response = self.app.get('/')
        self.assertIsInstance(response.data.decode('utf-8'), str)
        print("Test 4 reussi : La reponse est une chaine de caracteres")


if __name__ == '__main__':
    unittest.main()
