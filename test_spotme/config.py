""" List Pip:
- pip install pytube
- pip install flask_sqlalchemy
"""

from crypt import methods
from flask import *
import pytube as pt
import os
from flask_sqlalchemy import *
import pytube

app = Flask(__name__)

#CAMINHO PARA O BANCO
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'main.db')

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)