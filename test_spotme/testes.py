import string
from model import *
from config import *
import pytube

rock = Generos(nome = 'rock')
pop = Generos(nome = 'pop')
samba = Generos(nome = 'samba')
eletronica = Generos(nome = 'eletronica')
forro = Generos(nome = 'forro')
funk = Generos(nome = 'funk')
pagode = Generos(nome = 'pagode')
rap = Generos(nome = 'rap')
mpb = Generos(nome = 'mpb')


generos = [rock, pop, samba, eletronica,forro,funk,pagode,rap,mpb]
for i in generos:
    db.session.add(i)

db.session.commit()


"""indefinido = Generos(nome = 'indefinido')
db.session.add(indefinido)
db.session.commit()"""

"""genero = db.session.query(Musicas).filter_by(genero = 1).all()
print(*[x for x in genero])"""

