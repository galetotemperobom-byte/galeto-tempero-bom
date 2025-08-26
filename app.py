from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/pix')
def pix():
    return render_template('pix.html')

@app.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        hora = request.form['hora']
        obs = request.form['obs']
        print(f"Agendamento recebido: {nome}, {data}, {hora}, {obs}")
        return redirect('/')
    return render_template('agendamento.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

if __name__ == '__main__':
    app.run(debug=True)
