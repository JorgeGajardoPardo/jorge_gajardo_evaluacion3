from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ej1', methods=['GET', 'POST'])
def ej1():
    resultado = None
    if request.method == 'POST':
        try:
            n1 = int(request.form['n1'])
            n2 = int(request.form['n2'])
            n3 = int(request.form['n3'])
            asistencia = int(request.form['asistencia'])

            promedio = round((n1 + n2 + n3) / 3, 2)
            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

            resultado = {
                'promedio': promedio,
                'asistencia': asistencia,
                'estado': estado
            }
        except ValueError:
            resultado = {'error': 'Debes ingresar valores numéricos válidos.'}

    return render_template('ej1.html', resultado=resultado)


@app.route('/ej2', methods=['GET', 'POST'])
def ej2():
    resultado = None
    if request.method == 'POST':
        nombre1 = request.form['nom1']
        nombre2 = request.form['nom2']
        nombre3 = request.form['nom3']

        nombres = [nombre1, nombre2, nombre3]
        mayor = max(nombres, key=len)
        resultado = {
            'mayor': mayor,
            'largo': len(mayor)
        }

    return render_template('ej2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
