import unittest


class StatMixin:
    def send_stat(self, result):
        if result.wasSuccessful():
            print('ready')


class SkyProTestCase(StatMixin, unittest.TestCase):
    def run(self, *args, **kwargs):
        result = super().run(*args, **kwargs)
        self.send_stat(result)
        return result
