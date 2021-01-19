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
  - [X] Modelo de ATA de monografia
- [X] manual do estágio
- [X] grade curricular
  - [X] Figura dos pre-requisitos da parte optativa
- [ ] cadastro dos dos componentes curriculares optativos
- [ ] Cadastros dos componentes curriculares equivalentes:
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
