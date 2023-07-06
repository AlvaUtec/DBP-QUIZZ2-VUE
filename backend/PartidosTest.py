import unittest 
from config.local import config
from app.models import Partido, Lista
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import json
import io as io

class PartidosTests(unittest.TestCase):
    def setUp(self):
        database_path = config['DATABASE_URI']
        self.app = create_app({'database_path': database_path})
        self.client = self.app.test_client()

        self.new_partido = {
            'local': 'Alianza Lima',
            'visitante': 'Universitario',
            'estadio': 'Estadio Nacional',
            'lista': 'Lista 1'
        }

    def test_create_partido_success(self):
        response = self.client.post('/partidos', json=self.new_partido)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['partido_created_id'])


    def test_create_partido_failed_400(self):
        response = self.client.post('/partidos', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])