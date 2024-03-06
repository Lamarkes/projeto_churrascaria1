from flask import *
import dao
import dataanalise as da
import plotly.express as px

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def cadastrar_usuario():
    nome = str(request.form.get('nome'))
    senha = str(request.form.get('senha'))

    if dao.verificarlogin(nome, senha):
        return render_template('menu.html')
    else:
        return render_template('index2.html')

@app.route('/grafvioleciapib', methods=['POST','GET'])
def gerarGrafViolenciaPib():
    if request.method == 'POST':
        filtro = int(request.form.get('valor'))
    else:
        filtro = 10

    dados = da.lerdados()
    dados.drop(dados.sort_values(by=['cvli'], ascending=False).head(3).index, inplace=True)
    dados.drop(dados.sort_values(by=['rendapercapita'], ascending=False).head(filtro).index, inplace=True)
    dados.drop(dados.sort_values(by=['rendapercapita'], ascending=True).head(2).index, inplace=True)

    fig = px.scatter(dados, x='rendapercapita', y='cvli', hover_data=['municipio'])
    return render_template('grafviolenciapib.html', plot=fig.to_html())

@app.route('/grafcorrelacao')
def gerarGrafCorrelacao():
    dados = da.lerdados()
    fig2 = da.exibirmapacorrelacoes(dados)

    return render_template('grafcorrelacao.html', mapa=fig2.to_html())


@app.route('/melhoresedu', methods=['POST', 'GET'])
def exibirmunicipiosedu():
    if request.method == 'POST':
        filtro = int(request.form.get('valor'))
    else:
        filtro = 10

    data = da.lerdados()
    data['somaedu'] = data['idebanosiniciais'] + data['idebanosfinais']
    data.sort_values(by=['somaedu'], ascending=False, inplace=True)
    fig = da.exibirgraficobarraseduc(data.head(filtro))

    return render_template('melhoresedu.html', figura=fig.to_html())

@app.route('/idebanosiniciais', methods=['GET'])
def exibiranosiniciaisideb():
    data = da.lerdados()

    fig = da.exibirgraficopizzaidebanosiniciais(data.head(10))

    return render_template('idebanosiniciais.html', figura=fig.to_html())


@app.route('/graficoidebanosfinais', methods=['GET', 'POST'])
def exibiranosfinaisideb():
    if request.method == 'POST':
        filtro = int(request.form.get('valor'))
    else:
        filtro = 6
    dados = da.lerdados()

    fig = da.exibirgraficoideb(dados.head(filtro))

    return render_template('graficoideb.html', graf=fig.to_html())


@app.route('/grafidhpormunicipio', methods=['GET'])
def exibiridhrendapercapita():

    dados = da.lerdados()

    fig = da.exibiridhmunicipio(dados.head(5))

    return render_template('grafridh.html', fig=fig.to_html())


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/')
def motormanda():
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)