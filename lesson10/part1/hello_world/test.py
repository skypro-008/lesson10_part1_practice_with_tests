from utils import SkyProTestCase

from .task import app


class HelloWorldTestCase(SkyProTestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_page(self):
        with self.app as client:
            resp = client.get('/')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, 'Hello, World'.encode())
