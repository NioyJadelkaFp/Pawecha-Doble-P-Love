from flask import Flask,render_template
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcular_diferencia(fecha_inicio, fecha_final):
    diferencia = relativedelta(fecha_final, fecha_inicio)
    
    return diferencia.years, diferencia.months, diferencia.days


app = Flask(__name__)

@app.route('/')
def home():

    fecha_inicio = datetime(2017, 1, 1) 
    fecha_final = datetime.now() 
    años, meses, dias = calcular_diferencia(fecha_inicio, fecha_final)

    title = 'Contador'
    return render_template('home.html', title=title, años=años, meses=meses, dias=dias)

if __name__ == '__main__':
    app.run(debug=True, port=7000)