from flask import Flask,render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    title = "Home"
    with open('proyectos.json', 'r') as archivo:
        datos = json.load(archivo)
    return render_template('index.html', title=title, datos=datos)
    #return "index"

if __name__ == '__main__':
    app.run(debug=True)
