from flask import Flask,render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    title:str = "Home"

    with open('static/json/proyectos.json', 'r') as archivo:
        datos = json.load(archivo)

    return render_template('index.html', title=title, datos=datos)

if __name__ == '__main__':
    app.run(debug=True)











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