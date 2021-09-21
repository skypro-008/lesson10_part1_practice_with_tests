import random
import string

from utils import SkyProTestCase
from .task import app, load_users

USERS: list = load_users()
NOT_FOUND_ANSWER: str = 'Не найдено'


class FindUserTestCase(SkyProTestCase):

    def get_key(self):
        return "173645"

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_user_page(self):
        with self.app as client:
            resp = client.get('/users/1/')
            self.assertEqual(resp.status_code, 200, )

            random_string_id = ''.join(random.sample(string.ascii_lowercase, 6))
            resp = client.get('/users/{}/'.format(random_string_id))
            self.assertEqual(resp.status_code, 404)

            for id in (0, 11, 20, 100, 1000):
                resp = client.get(f'/users/{id}', follow_redirects=True)
                self.assertEqual(resp.status_code, 404)
                self.assertEqual(resp.data, NOT_FOUND_ANSWER.encode())

            resp = client.get('/users/1', follow_redirects=True)
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, 'Wong Gordon'.encode())

            resp = client.get('/users/2', follow_redirects=True)
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, 'Blankenship Church'.encode())
