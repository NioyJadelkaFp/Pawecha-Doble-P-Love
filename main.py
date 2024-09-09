from flask import Flask,render_template
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import requests
import pprint

def calcular_diferencia(fecha_inicio, fecha_final):
    diferencia:int = relativedelta(fecha_final, fecha_inicio)
    
    return diferencia.years, diferencia.months, diferencia.days


app = Flask(__name__)

@app.route('/')
def index():
    title:str = "Home"
    with open('static/json/infoweb.json', 'r') as file:
        data = json.load(file)

    return render_template('index.html', data=data, title=title)

@app.route('/hola')
def hola():
    title:str = 'Hola Mundo'
    return render_template('hola.html',title=title)

@app.route('/memes')
def meme():
    url = "https://www.reddit.com/r/memexico/.json"
    headers = {'User-agent': 'your bot 0.1'}
    response = requests.get(url, headers=headers)
    data = response.json()
    memes = data['data']['children'][:1000]  # Obtener los primeros 10 memes
    return render_template('memes.html', memes=memes)











#Hr pawecha 
@app.route('/horadepawecha')
def home():

    fecha_inicio:int = datetime(2017, 1, 20) 
    fecha_final = datetime.now() 
    años, meses, dias = calcular_diferencia(fecha_inicio, fecha_final)

    title = 'Contador'
    return render_template('home.html', title=title, años=años, meses=meses, dias=dias)

if __name__ == '__main__':
    app.run(debug=True, port=7000)