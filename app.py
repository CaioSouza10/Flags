from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/buscar', methods=['POST'])
def buscar():
    nome_pais = request.form.get('país')
    url = f'https://restcountries.com/v3.1/name/{nome_pais}'
    resposta = requests.get(url)
    dados = resposta.json()
    if isinstance(dados, list):
        lista_final = dados
    else:
        lista_final = [] # Se não achar nada, manda uma lista vazia
        
    return render_template('index.html', all_paises=lista_final, nome_usuario='Caio')


@app.route('/')
def index():
    url = 'https://restcountries.com/v3.1/all'
    resposta = requests.get(url)
    dados = resposta.json()
    if isinstance(dados, list):
        lista_final = dados
    else:
        lista_final = []
    print(dados)        
    return render_template('index.html', all_paises=lista_final, nome_usuario='Caio')


if __name__ == '__main__':
    app.run(debug=True)



   