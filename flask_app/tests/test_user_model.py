import unittest
from api.models import User
from api import create_app, sql


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.app_context = self.app.app_context()
        self.app_context.push()
        sql.create_all()

    def tearDown(self):
        sql.session.remove()
        sql.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        """
        Test the password setter of user model
        """
        u = User(password="hello")
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        """
        Test wheather the password getter will raise an error
        """
        u = User(password="hello")
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        """
        Test password verification
        """
        u = User(password="hello")
        self.assertTrue(u.verify_password("hello"))
        self.assertFalse(u.verify_password("world"))

    def test_random_salts_passwords(self):
        """
        Tests whether the salting is random
        """
        u = User(password="hello")
        u1 = User(password="hello")
        self.assertTrue(u.password_hash != u1.password_hash)
