import unittest
from app import app, users_db

class TestApp(unittest.TestCase):

    def setUp(self): 
        self.app = app.test_client()
        users_db.clear()

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_get_user_not_found(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        response = self.app.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(users_db), 1)

    def test_create_user_invalid(self):
        response = self.app.post('/users', json={})
        self.assertEqual(response.status_code, 400)

    def test_update_user(self):
        self.app.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.app.patch('/users/1', json={"name": "Wojtek"})
        self.assertEqual(response.status_code, 204)
        self.assertEqual(users_db[0]['name'], "Wojtek")

    def test_update_user_invalid(self):
        response = self.app.patch('/users/1', json={})
        self.assertEqual(response.status_code, 400)

    def test_update_user_not_found(self):
        response = self.app.patch('/users/1', json={"name": "Wojtek"})
        self.assertEqual(response.status_code, 404)

    def test_replace_user(self):
        self.app.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.app.put('/users/1', json={"name": "Wojtek", "lastname": "Nowak"})
        self.assertEqual(response.status_code, 204)
        self.assertEqual(users_db[0]['name'], "Wojtek")
        self.assertEqual(users_db[0]['lastname'], "Nowak")

    def test_replace_user_invalid(self):
        response = self.app.put('/users/1', json={})
        self.assertEqual(response.status_code, 400)

    def test_replace_user_not_found(self):
        response = self.app.put('/users/1', json={"name": "Wojtek", "lastname": "Nowak"})
        self.assertEqual(response.status_code, 404)

    def test_delete_user(self):
        self.app.post('/users', json={"name": "Wojciech", "lastname": "Oczkowski"})
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(users_db, [])

    def test_delete_user_not_found(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
