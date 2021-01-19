"""
Script para gerar a figura da integralização curricular.
"""

import json
from pathlib import Path
from graphviz import Digraph

OPTIONS = {
    'digraph_name': 'Integralização Curricular',
    'comment': 'Gerado pelo script generate_figure_integralizacao.py',
    'directory': 'assets/images',
    'format': 'svg',
    'engine': None,
    'encoding': 'utf-8',
    'graph_attr': {
        'bgcolor': 'transparent',
        'rankdir': 'TD',
        'ranksep': '2'
    },
    'node_attr': {
        'shape': 'rect',
        'style': 'rounded',
    },
    'edge_attr': None,
    'body': None,
    'strict': False
}


def load(caminho):
    """Carrega todos os componentes especificados pelo caminho do arquivo passado como parâmetro."""
    p = Path(caminho)
    componentes_todos = []
    for x in p.iterdir():
        with x.open('r', encoding='utf8') as file:
            componentes_todos.append(json.load(file))
    return componentes_todos


def seleciona_componentes(componentes, tipos):
    """Seleciona somente os componentes com o tipo passado como parâmetro."""
    # seleciona todos os componentes do tipo especificado.
    componentes_selecionados = [
        componente for componente in componentes
        if componente['curso']['carater'] in tipos
    ]
    cod_componentes_selecionados = [
        componente['codigo'] for componente in componentes_selecionados
    ]

    # pega a lista de códigos de todos os prerequisitos dos componentes
    prerequisitos = []
    for componente in componentes_selecionados:
        for cod_prerequisito in componente.get('pre-requisitos', []):
            prerequisitos.append(cod_prerequisito)

    # descobre quais pre-requisitos estão faltando
    prerequisitos = [
        cod_prerequisito for cod_prerequisito in prerequisitos
        if cod_prerequisito not in cod_componentes_selecionados
    ]

    # adiciona esses prerequisitos na lista de componentes selecionadas
    for componente in componentes:
        if componente['codigo'] in prerequisitos:
            componentes_selecionados.append(componente)
    return componentes_selecionados


def pares_prerequisitos(componentes_selecionados):
    pares_prereqs = []
    for componente in componentes_selecionados:
        for cod_prereq in componente.get('pre-requisitos', []):
            for prerequisito in componentes_selecionados:
                if cod_prereq == prerequisito['codigo']:
                    pares_prereqs.append((prerequisito, componente))
    return pares_prereqs


def faz_grafico(nome_arquivo, tipo_componente=None):
    """Faz o gráfico com os componentes obrigatórios ou eletivos."""
    integralizacao = Digraph(name=OPTIONS['digraph_name'],
                             comment=OPTIONS['comment'],
                             filename=nome_arquivo,
                             directory=OPTIONS['directory'],
                             format=OPTIONS['format'],
                             engine=OPTIONS['engine'],
                             encoding=OPTIONS['encoding'],
                             graph_attr=OPTIONS['graph_attr'],
                             node_attr=OPTIONS['node_attr'],
                             edge_attr=OPTIONS['edge_attr'],
                             body=OPTIONS['body'],
                             strict=OPTIONS['strict'])
    componentes_todos = load("./_data/componentes-curriculares")
    componentes_selecionados = seleciona_componentes(componentes_todos,
                                                     tipo_componente)

    # calcula o maior semestre do curso para fazer a clusterização do gráfico.
    max_semestres = 0
    for componente in componentes_selecionados:
        max_semestres = max(max_semestres,
                            componente['curso'].get('semestre', -1))

    # semestre['i'] guarda as componentes do i-esimo semestre.
    semestre = {}
    for x in range(1, max_semestres + 1):
        semestre[str(x) + "º Semestre"] = [
            componente for componente in componentes_selecionados
            if componente['curso'].get('semestre') == x
        ]
    semestre['Nenhum'] = [
        componente for componente in componentes_selecionados
        if componente['curso'].get('semestre') == None
    ]

    # adiciona os nós das componentes de cada semestre.
    for nome, componentes in semestre.items():
        with integralizacao.subgraph(name='cluster_' + str(nome)) as c:
            c.attr(pencolor='black', style='rounded', label=nome, tooltip=nome)
            for componente in componentes:
                c.node(componente['codigo'],
                       label=componente['codigo'],
                       href='../../curso/componentes/' +
                       componente['codigo'].lower() + '.html',
                       tooltip=componente['nome'])

    # adiciona as arestas entre os pre-requisitos e seus componentes.
    pre_requisitos = pares_prerequisitos(componentes_selecionados)
    edges = []
    for prereq, componente in pre_requisitos:
        edges.append((prereq['codigo'], componente['codigo']))
    integralizacao.edges(edges)
    integralizacao.render()


def main():
    faz_grafico('integralizacao-curricular.gv', ['Obrigatório', 'Eletivo'])
    faz_grafico('integralizacao-curricular-optativos.gv', ['Optativo'])
    faz_grafico('integralizacao-curricular-todos.gv',
                ['Obrigatório', 'Optativo', 'Eletivo'])


if __name__ == '__main__':
    main()