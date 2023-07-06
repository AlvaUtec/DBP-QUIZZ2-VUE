from flask_sqlalchemy import SQLAlchemy
from config.local import config
import uuid
from datetime import datetime
import sys


db = SQLAlchemy()

def setup_db(app, database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = config['DATABASE_URI'] if database_path is None else database_path
    db.app = app
    db.init_app(app)
    db.create_all()


class Partido(db.Model):
    __tablename__ = 'partidos'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    equipo_local = db.Column(db.String(120), nullable=False)
    equipo_visitante = db.Column(db.String(120), nullable=False)
    estadio = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    list_id = db.Column(db.String(36), db.ForeignKey('listas.id'), nullable=True)


    def __init__(self, equipo_local, equipo_visitante, estadio, l_key):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.estadio = estadio
        self.list_id = l_key
        self.created_at = datetime.utcnow()
        
    def __repr__(self):
        return '<Partido %r %r>' % (self.equipo_local, self.equipo_visitante)
    
    def serialize(self):
        return {
            'id': self.id,
            'equipo_local': self.equipo_local,
            'equipo_visitante': self.equipo_visitante,
            'estadio': self.estadio,
            'list_id': self.list_id,
            'created_at': self.created_at
        }
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            raise e
        finally:
            _id = self.id
            db.session.close()
            return _id


class Lista(db.Model):
    __tablename__ = 'listas'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    partido = db.relationship('Partido', backref='lista', lazy=True)

    def __init__(self, nombre):
        self.nombre = nombre
        self.created_at = datetime.utcnow()
        
    def __repr__(self):
        return '<Lista %r>' % (self.nombre)
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'created_at': self.created_at
        }
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(sys.exc_info())
            db.session.rollback()
            raise e
        finally:
            _id = self.id
            db.session.close()
            return _id
