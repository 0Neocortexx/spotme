from config import *

class Generos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    def __str__(self):
        return f'id: {self.id}, nome: {self.nome}'
    
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome
        }

class Musicas(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(254))
    artista = db.Column(db.String(254))
    link = db.Column(db.String(254))

    generos_id = db.Column(db.Integer, db.ForeignKey(Generos.id), nullable=False)
    generos = db.relationship("Generos")

    def __str__(self):
        return f'ID: {self.id}, Gênero: {self.generos.json()}, Nome da música: {self.nome}, Artista: {self.artista}, Link para musica: {self.link}'

    def json(self):
        return {
            "id": self.id,
            "genero": self.generos.json(),
            "nome": self. nome,
            "artista": self.artista,
            "link": self.link
        }
        
if __name__ == "__main__":
    db.create_all()