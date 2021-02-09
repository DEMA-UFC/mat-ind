---
title: Coordenação
coordenador: Ronan Pardo Soares
vice-coordenador: Michael Ferreira de Souza
secretaria: Cláudia Damasceno Maia
email: miufc@ufc.br
unidades-curriculares:
- unidade: Métodos Matemáticos
  membro: Michael Ferreira de Souza
  suplente: Carlos Diego Rodrigues 
- unidade: Métodos Estatísticos
  membro: João Welliandre Carneiro Alexandre
  suplente: Sílvia Maria de Freitas
- unidade: Métodos Computacionais
  membro: Ronan Pardo Soares
  suplente: Albert Einstein Fernandes Muritiba
- unidade: Matemática Aplicada
  membro: Manoel Bezerra Campêlo Neto
  suplente: Rafael Castro de Andrade
- unidade: Formação Complementar
  membro: Ricardo Coelho Silva
  suplente: Maria Jacqueline Batista
- unidade: Representante Discente
  membro: Francisco Claudio Costa Moraes Junior
  suplente: Pedro Henrique Sousa da Silva
nde:
- Albert Einstein Fernandes Muritiba
- Carlos Diego Rodrigues
- Jesus Ossian da Cunha Silva
- Michael Ferreira de Souza
- Ronan Pardo Soares
vigencia-coordenacao-inicio: 2019-03-01
vigencia-coordenacao-fim: 2022-02-28
vigencia-nde-inicio: 2020-09-08
vigencia-nde-fim: 2023-09-08
atas-colegiado:
- 2020-09-08
- 2020-07-17
- 2019-11-12
- 2019-08-05
- 2019-04-23
- 2019-02-18
- 2018-12-14
- 2018-11-09
- 2017-10-24
- 2017-05-30
- 2017-04-25
- 2016-12-19
- 2016-05-25
- 2014-12-02
- 2014-09-29
- 2014-03-27
- 2013-12-12
- 2013-10-11
- 2013-06-05
- 2013-05-16
- 2013-01-10
- 2012-11-30
- 2012-11-13
- 2012-05-07
- 2012-02-27
- 2011-12-08
- 2011-11-29
- 2011-11-07
- 2011-10-17
- 2011-10-05
- 2011-07-04
- 2011-05-19
- 2011-04-07
- 2010-12-03
- 2010-11-30
atas-nde:
- 2020-12-09
- 2021-01-27
- 2021-02-03
---

# {{ page.title }}

A coordenação do curso de matemática industrial com vigência de {{ page.vigencia-coordenacao-inicio | date: "%d/%m/%Y" }} até {{ page.vigencia-coordenacao-fim | date: "%d/%m/%Y" }} é regulamentada pela [Portaria Nº 1124 PROGEP de 2019](../assets/pdfs/coordenacao/vigencia-coordenacao-2019-03-01-2022-02-28.pdf).

## Servidores da Coordenação

- Coordenador: {{ page.coordenador }}
- Vice-coordenador: {{ page.vice-coordenador }}
- Secretária: {{page.secretaria }}
- Email: [miufc@ufc.br](mailto:{{ page.email }})

## Colégiado da Coordenação

O colégiado da coordenação é composto pelos seguintes membros:

| Unidade | Membro | Suplente |
| ------- | ------ | -------- |
{% for item in page.unidades-curriculares -%}
|{{ item.unidade }} | {{ item.membro }} | {{ item.suplente }}|
{% endfor %}

O colegiado tem vigência de {{ page.vigencia-coordenacao-inicio | date: "%d/%m/%Y" }} até {{ page.vigencia-coordenacao-fim | date: "%d/%m/%Y" }} tendo sido outorgado pelo resultado de [eleição departamental](../assets/pdfs/coordenacao/vigencia-colegiado-2019-03-01-2022-02-28.pdf).

## O Núcleo Docente Estruturante

Os membros do atual Núcleo Docente Estruturante são:

{% for item in page.nde %}
- {{ item }}
{% endfor %}

A vigência desse colégiado vai de {{ page.vigencia-nde-inicio | date: "%d/%m/%Y" }} até {{ page.vigencia-nde-fim | date: "%d/%m/%Y" }} tendo sido regulamentado pela [Portaria Nº 20 Centro de Ciências de 2020](../assets/pdfs/coordenacao/vigencia-nde-2020-09-08-2023-09-08.pdf).

## Atas de Reuniões

### Reuniões do Colégiado

{% for data in page.atas-colegiado %}
- [{{ data | date: "%d/%m/%Y" }}](atas/colegiado-{{ data }}.html)
{% endfor %}

### Reuniões do NDE

{% for item in page.atas-nde %}
- [{{ item | date: "%d/%m/%Y" }}](atas/nde-{{ item }}.html)
{% endfor %}

## Outros Documentos
