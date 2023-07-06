import unittest 
from config.local import config
from app.models import Lista
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import io as io

class ListasTests(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.app = create_app({'database_path': database_path})
        self.client = self.app.test_client()

        self.new_lista = {
            'name': 'Lista 1',
        }
    
    def test_create_lista_success(self):
        response = self.client.post('/listas', json=self.new_lista)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['lista_created_id'])


    def test_create_lista_failed_400(self):
        response = self.client.post('/listas', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])