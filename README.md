# PPC Matemática Industrial

Esse é o repositório para a criação do site do curso de Matemática Industrial da UFC.
Aqui você pode encontrar os arquivos utilizados para gerar o site usando o [Jekyll](https://jekyllrb.com).
As figuras são geradas dinamicamente através do [Python](https://www.python.org) utilizando a biblioteca [graphviz](https://github.com/xflr6/graphviz) e o aplicativo [Graphviz](https://graphviz.org)

Para ter um ambiente funcionando de forma que você seja capaz de rodar todo o site localmente e fazer suas alterações no ambiente [Ubuntu](https://ubuntu.com), siga os seguintes passos:

- Instalar o [Jekyll no Ubuntu](https://jekyllrb.com/docs/installation/ubuntu).
- Instale o Python3 no Ubuntu (se ele não estiver instalado).
- Instale o pip do Python3: `sudo apt install python3-pip`
- Instale o Graphviz: `sudo apt install graphviz`
- Instale a api do graphviz pro Python3: `pip3 install graphviz`
- Para gerar localmente o site e rodar um servidor: `bundle exec jekyll b; bundle exec jekyll s`
- Para acessar o site localmente: <http://localhost:4000>

## Tarefas por fazer

- [X] manual de atividades complementares
- [X] atividades de extensão
- [X] publicar no github
- [X] automatizar *build* no github
- [X] página da coordenação
- [X] página do NDE
- [X] manual da monografia
  - [X] Formulário do plano de trabalho da monografia
  - [X] Formulário de substituição de orientador
  - [X] Formulário de sugestão de banca
  - [X] modelo de ATA de monografia
- [X] manual do estágio
- [X] grade curricular
  - [X] figura dos pre-requisitos da parte optativa
- [ ] [verificar adequação do manual de estágio](#adequação-manual-de-estágio)
- [ ] [verificar adequação do manual de estágio](#adequação-manual-de-monografia)
- [ ] [verificar adequação do manual de atividades complementares](#adequação-manual-de-atividades-complementares)
- [ ] tabela de disciplinas e pedido de ementário atualizado
- [ ] adastro dos dos componentes curriculares optativos
- [ ] cadastros dos componentes curriculares equivalentes:
  - [ ] CK0030
  - [ ] CC0287
  - [ ] CK0235
  - [ ] HC0747
  - [ ] CK0175
  - [ ] EH0027
  - [ ] EH0287
  - [ ] PD0077
- [ ] página das perguntas frequentes
- [ ] alterações na página do PPC
  - [ ] figura de pré-requisitos geral
  - [ ] tabela de pré-requisitos
  - [ ] tabela ix.2. distribuição da carga didática da matriz curricular do curso de bacharelado em matemática industrial página 39
  - [ ] tabela ix.3. integralização curricular do curso de matemática industrial 2011.1 página 40
  - [ ] tabela ix.4. composição das unidades curriculares do curso de matemática industrial página 41
  - [ ] tabela ix.4. relação de disciplinas por departamento de origem
- [ ] script de construção total
- [ ] explicar o funcionamento do schema e como validar e inserir uma disciplina
- [ ] explicar como fazer contribuições
- [ ] adicionar pdfs ao final de cada um dos componentes
- [ ] adicionar atas do NDE e Colegiado ao sistema
- [ ] página inicial
- [ ] refazer logomarca
- [ ] preparar logo do DEMA
- [ ] colocar cores na figura de integralização curricular
- [ ] colocar carga-horária nas disciplinas do SIGAA
- [ ] converter as atas para o sei

### Adequação Manual de Estágio

Verificar a adequação do manual de estágio com os seguintes itens:

[Lei Nº 11.788, de 25 de setembro de 2008](http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm)
[Resolução Nº 32 de 30 de outubro de 2009 do CEPE/UFC](http://www.ufc.br/images/_files/a_universidade/cepe/resolucao_cepe_2009/resolucao32_cepe_2009.pdf)
[Portaria Nº 123 de 31 de agosto de 2018 do Gabinete do Reitor/UFC](../assets/pdfs/externo/portaria-gr-123-2018-08-31.pdf)
[Manual de Estágio da UFC](https://prograd.ufc.br/wp-content/uploads/2013/11/manual-de-estagio-da-ufc.pdf)

#### Tarefas

- [ ] Adicionar no SEI a Normatização do Estágio
  - [ ] Adicionar Ofícios e/ou atas de reunião com datas de aprovação da normatização pelo Colegiado da Coordenação e pelo Conselho da Unidade Acadêmica;
- [ ] Adicionar no SEI Manual de normatização do Estágio Curricular Supervisionado (com seus respectivos anexos, quando for o caso).
- [ ] O Manual de normatização do Estágio Curricular Supervisionado, dentre outros aspectos, deve contemplar:
  - [ ] Indicação dos documentos legais que serviram de embasamento à elaboração do
manual, tais como:
    - [ ] Lei de Diretrizes e Bases da Educação Nacional (art. 82) – Lei No 9.394, de 20 de dezembro de 1996;
    - [ ] Projeto Pedagógico do Curso;
    - [ ] Regimento Geral da UFC;
    - [ ] Resolução No 12/CEPE, de 19 de junho de 2008, que Dispõe sobre procedimentos a serem adotados em casos de “Reprovação por Frequência” na UFC;
    - [ ] Resolução No 32/CEPE, de 30 de outubro de 2009, que Disciplina o Programa de Estágio Curricular Supervisionado para os estudantes dos Cursos Regulares da UFC;
    - [ ] Lei 11.788, de 25 de setembro de 2008, que dispõe sobre estágio de estudantes;
    - [ ] Resolução CNE/CES N° 02, de 18 de junho de 2007, que dispõe sobre carga horária mínima e procedimentos relativos à integralização e duração dos cursos de graduação, bacharelados, na modalidade presencial;
    - [X] Diretrizes Curriculares Nacionais do Curso; (**não temos**)
    - [ ] Parecer CNE/CES No 416/2012, aprovado em 8 de novembro de 2012, que trata de consulta sobre estágio no exterior;
    - [ ] Resolução No 23/CEPE, de 03 de outubro de 2014, que estabelece normas visando a fortalecer o ensino de graduação e de pós-graduação, a pesquisa e a extensão, ao fixar o regime de trabalho e carga horária dos professores do Magistério Superior da UFC, e dá outras providências.
  - [ ] Definição do Estágio Curricular Supervisionado no Curso, em consonância com a Lei 11.788, de 25 de setembro de 2008, a - Resolução 32/2009 (arts. 3o, 5o e 6o) e o Projeto Pedagógico do Curso, levando em conta os seguintes aspectos:
    - [ ] Indicação do caráter do estágio no curso: se obrigatório e/ou não obrigatório;
    - [ ] Natureza das atividades a serem consideradas como estágio;
    - [ ] Designação dos locais onde o estudante poderá estagiar;
    - [ ] Determinação da carga horária máxima semanal a ser cumprida pelo estagiário (em conformidade com o Capítulo IV da Lei 11.788).
  - [ ] Dissertação sobre importância do Estágio Curricular Supervisionado para o curso e para a formação do aluno;
  - [ ] Indicação da obrigatoriedade da integralização da carga horária do Estágio Curricular Supervisionado como requisito para a colação de grau do aluno (nos casos de estágio obrigatório);
  - [ ] Apresentação dos objetivos do manual (gerais e específicos, se for o caso);
  - [ ] Contextualização do Estágio na integralização curricular do Curso (conforme PPC);
  - [ ] Indicação da carga horária do Estágio Curricular Supervisionado no Curso (conferidos PPC e SIGAA), e conforme Resolução CNE/CES n° 02/2007, art. 1o, Parágrafo Único (estágios e atividades complementares para bacharelados presenciais não deverão exceder a 20% da carga horária total);
  - [ ] Definição da natureza do estágio (individual ou em grupo);
  - [ ] Indicação das partes envolvidas na atividade de estágio (coordenação do curso; estagiário; orientador; supervisor de estágio, dentre outros) com definição dos direitos (quando for o caso) e deveres/atribuições de cada um;
  - [ ] Designação de critérios de matrícula/registro do Estágio Curricular Supervisionado;
  - [ ] Designação dos tipos de documentos de formalização da realização da atividade de estágio (Termo de Compromisso ou Declaração de Estágio, Relatórios de Atividade, Plano de Trabalho, Apólice de Seguro, etc.), a serem apresentados pelo aluno, levando em conta os documentos disponíveis no site da Agência de Estágios da UFC, e indicando a quem esses documentos devem ser entregues;
  - [ ] Indicação do documento final de avaliação a ser entregue pelo estagiário (monografia, artigo, relatório), com as formatações definidas;
  - [ ] Determinação de prazos para entrega (e para revisão) do documento de avaliação e no de vias necessárias;
  - [ ] Estabelecimento de critérios de aprovação no estágio, com base no Regimento Geral da UFC (art. 116, § 2o), na Resolução CEPE 32/2009 e na Resolução CEPE 12/2008 (art. 1o, § 1o):
    - [ ] Nota (igual ou superior a 7,0);
    - [ ] Frequência (igual ou superior a 90%);
    - [ ] Qualificação (conhecimentos, habilidades requeridas do aluno);
  - [ ] Definição de procedimentos a serem adotados pelo curso no acompanhamento do aluno não aprovado;
  - [ ] Inclusão (em anexos) dos modelos de documentos/formulários a serem preenchidos e entregues pelo aluno;
  - [ ] Previsão de resolução de casos omissos (a quem compete e qual prazo para resposta).

### Adequação Manual de Monografia

### Adequação Manual de Atividades Complementares
