import unittest
from api.models import User
from api import create_app, sql
from flask_jwt_extended import create_access_token

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        sql.create_all()
        self.client = self.app.test_client()
        
        user=User(username='test', password='test password')
        sql.session.add(user)
        sql.session.commit()
        self.user=user

    
    def tearDown(self):
        sql.session.remove()
        sql.drop_all()
        self.app_context.pop()
    
    def get_tokens(self):
        return create_access_token(identity=self.user, fresh=True)
    
    def test_v1_home(self):
        """v1 home route testing
        """
        response = self.client.get(
            '/v1/', content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
    
    def test_no_auth(self):
        """
        Test protected routes are no accessable without token
        """
        response = self.client.get('/v1/profile')
        self.assertEqual(response.status_code , 401)
    
    def test_auth_login(self):
        """
        Test the auth/login route
        """
        response=self.client.post(
            '/auth/login', json={'username':'test', 'password':'test password'}
        )
        self.assertEqual(response.status_code, 200)
        
    
    def test_v1_token(self):
        """
        Test the v1/profile route
        """
        token=self.get_tokens()
        response = self.client.get('/v1/profile', headers={'Authorization': f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)