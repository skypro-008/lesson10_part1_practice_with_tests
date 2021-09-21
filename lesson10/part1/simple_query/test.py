from utils import SkyProTestCase
import string

from .task import app

URL_PATH: str = '/search/?s={}'


class SimpleQueryTestCase(SkyProTestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_search_page(self):
        with self.app as client:
            resp = client.get(URL_PATH.format('123'))
            self.assertEqual(resp.status_code, 200)    # "Запрос к /search/?s=... не обрабатывается"

            resp = client.get(URL_PATH.format('мос'))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, 'Москва'.encode())   # Неверный ответ при запросе /search/?s=мос"

            resp = client.get(URL_PATH.format('кра'))
            self.assertEqual(resp.status_code, 200)
            self.assertSetEqual(set(resp.data.decode().split(', ')), {'Красноярск', 'Краснодар'})  # Неверный ответ при запросе /search/?s=кра"

            resp = client.get(URL_PATH.format('санкт'))
            self.assertEqual(resp.status_code, 200, "При запросе "+URL_PATH.format('санкт')+"Неверный статус код") # Неверный код ответа при запросе /search/?s=санкт"
            self.assertEqual(resp.data, 'Санкт-Петербург'.encode())   # Неверный ответ при запросе /search/?s=санкт"

            resp = client.get(URL_PATH.format(string.ascii_lowercase[:5]))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, 'Городов не найдено'.encode())   # Неверный ответ если городов не найдено



