from flask import Flask, render_template, jsonify
from database import carrega_vagas_db, carrega_vaga_db

app = Flask(__name__)


# Rota Home
@app.route('/')
def hello():
  vagas = carrega_vagas_db()
  return render_template('home.html', vagas=vagas)


# Endpoint
@app.route('/vagas')
def lista_vagas():
  vagas = carrega_vagas_db()
  return jsonify(vagas)


@app.route('/vaga/<id>')
def mostra_vaga(id):
  vaga = carrega_vaga_db(id)
  if not vaga:
    return 'Not Found', 404
  return render_template('detalhevaga.html', vaga=vaga)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
