import pandas as pd
import plotly.express as px



def analisar():
    dados = pd.read_html('https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_taxa_de_homic%C3%ADdios')
    mais250 = dados[0]
    menores = dados[1]
    print(dados[0])


def lerdados():
    dados = pd.read_csv('dadosindicadoresPB3.csv')
    #excluir colunas
    dados.drop(columns=['code'], inplace=True)
    return dados


def exibirmapacorrelacoes(data):
    data.drop(columns=['municipio'], inplace=True)
    fig = px.imshow(data.corr())
    return fig


def exibirgraficobarraseduc(dados):
   # print(dados)
    fig = px.bar(dados, x='municipio', y='somaedu')
    return fig


def exibirgraficopizzaidebanosiniciais(dados):

    fig = px.pie(dados, values='idebanosiniciais', names='municipio')
    return fig


def exibirgraficoideb(dados):

    fig = px.line(dados, x='municipio', y='idebanosfinais')

    return fig


def exibiridhmunicipio(dados):

    fig = px.scatter(dados, x='idh', y='municipio', render_mode='webgl')
    fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))

    return fig
