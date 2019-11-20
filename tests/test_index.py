<<<<<<< HEAD
import unittest
from flask import url_for
from app import create_app


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()


    def test_status_code_deve_retornar_200(self):
        result = self.client.get(url_for('home.home_index'))

        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
=======
import pytest


>>>>>>> 3133a2d4f9d9333da950f57233074bfb2fda1e01
