import unittest
from flask import current_app
from api import create_app, sql


class BasicTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("test")
        self.app_context = self.app.app_context()
        self.app_context.push()
        sql.create_all()

    def tearDown(self) -> None:
        sql.session.remove()
        sql.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        """
        Test if the app is runnig
        """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """
        Ensuring it is running in test mode
        """
        self.assertTrue(current_app.config["TESTING"])
