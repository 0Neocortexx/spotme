from config import *
from model import *

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/inserir', methods=['GET', 'POST'])
def inserir_musica():
    if request.method == 'GET':
        return render_template('inserir.html')
    else:
        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
        data = request.get_json(force=True)
        print(data)
        try:
            procurarMusica =  db.session.query()
            new = Musicas(**data)
            db.session.add(new)
            db.session.commit()
            print("Operação Realizada!")

        except Exception as e:
            print(e)
            resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
        resposta.headers.add("Access-Control-Allow-Origin","*")
        return resposta


@app.route('/lista', methods=['GET'])
def exibir_lista():
    return render_template('listar.html')


# curl localhost:5000/listar
@app.route('/listar', methods=['GET'])
def listar():
        musicas = db.session.query(Musicas).all()
         # aplicar o método json que a classe Pessoa possui a cada elemento da lista
        musicas_em_json = [x.json() for x in musicas ]
        # converter a lista do python para json
        resposta = jsonify(musicas_em_json)
        # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta # retornar...

app.run(debug=True, host='0.0.0.0')