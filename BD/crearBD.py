import sqlalchemy as db
import pandas as pd
import os

os.chdir("..")
engine = db.create_engine('sqlite:///API/almacenamiento/basededatos/api.sqlite')
connection = engine.connect()
metadata = db.MetaData()

#CREAR TABLA INFO_SERVIDOR

info_servidorTab = db.Table('info_servidor',metadata,
                    db.Column('ID_SERVIDOR', db.Integer, primary_key = True, autoincrement = True),
                    db.Column('informacion_procesador', db.String(200)),
                    db.Column('informacion_procesador2',db.String(200)),
                    db.Column('nombre_SO', db.String(200)),
                    db.Column('version_SO', db.String(200)),
                    db.Column('ip_address', db.String(50)),
                    db.Column('fecha', db.DateTime())
                    )

#CREAR TABLA USUARIOS

usuariosTab = db.Table('usuarios',metadata,
                       db.Column('ID_USUARIO', db.Integer, primary_key = True, autoincrement = True),
                       db.Column('ID_SERVIDOR', db.Integer, db.ForeignKey("info_servidor.ID_SERVIDOR", onupdate = 'CASCADE'), nullable = False),
                       db.Column('name', db.String(200)),
                       db.Column('pid', db.Integer)       
                       )
   
#CREAR TABLA PROCESOS

ProcesosTab = db.Table('Procesos',metadata,
                db.Column('ID_PROCESO', db.Integer, primary_key = True, autoincrement = True),
                 db.Column('ID_SERVIDOR', db.Integer, db.ForeignKey("info_servidor.ID_SERVIDOR", onupdate = 'CASCADE'), nullable = False),
                 db.Column('name', db.String(200)),
                 db.Column('pid', db.Integer)
                 )

metadata.create_all(engine)
