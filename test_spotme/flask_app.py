from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pytube
import os

app = Flask(__name__)

#CAMINHO PARA O BANCO
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'main.db')

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)