from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [{
  'id': 1,
  'titulo': 'Analista de Dados',
  'localidade': 'RJ, Brasil',
  'salario': 'R$ 5.000,00'
}, {
  'id': 2,
  'titulo': 'Desenvolvedor Backend',
  'localidade': 'PR, Brasil',
  'salario': 'R$ 4.000,00'
}, {
  'id': 3,
  'titulo': 'Desenvolvedor de Software',
  'localidade': 'SP, Brasil',
  'salario': 'R$ 8.500,00'
}, {
  'id': 4,
  'titulo': 'Desenvolvedor Frontend',
  'localidade': 'RS, Brasil',
  'salario': 'R$ 6.500,00'
}, {
  'id': 5,
  'titulo': 'Cientista de Dados',
  'localidade': 'BH, Brasil',
  'salario': 'R$ 9.500,00'
}]


# Rota Home
@app.route('/')
def hello():
  return render_template('home.html', vagas=VAGAS)


# Endpoint
@app.route('/vagas')
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
