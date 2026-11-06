# Aula 14 — Flask + CRUD + JSON + MVC

> Material unificado a partir dos roteiros 0 a 6.

## Conteúdo

1. Visão geral: Flask, CRUD, JSON, MVC e Blueprint
2. Estrutura do projeto
3. Arquivos base: `base.html`, `config.py` e `app.py`
4. Views para adicionar e visualizar tarefas
5. View para editar tarefas
6. Model: lógica de negócio e acesso ao JSON
7. Controller: rotas e Blueprint

---

<!-- Fonte: roteiro.md -->

# Aula 14: FLASK + CRUD + JSON + MVC

### Esqueleto do Sistema SEM BLUEPRINT

SISTEMA (app.py)
│
├── Produtos
│   ├── cadastrar
│   ├── listar
│   ├── consultar
│   ├── editar
│   └── excluir
│
├── Usuários
│   ├── login
│   ├── logout
│   └── cadastro
│
└── Relatórios
    ├── gerar
    └── consultar


### Esqueleto do Sistema COM BLUEPRINT

SISTEMA
│
├── produtos
│   └── routes.py       ← Blueprint de produtos
│
├── usuarios
│   └── routes.py       ← Blueprint de usuários
│
├── relatorios
│   └── routes.py       ← Blueprint de relatórios
│
└── app.py              ← aplicação principal

---

<!-- Fonte: roteiro1.md -->

# Aula 14 - Padrão MVC para Projetos com Flask e JSON 
## Uso do CRUD To...DO

**Roteiro 1. ESTRUTURA DO PROJETO**

Para exemplificar o uso do padrão MVC em projetos de aplicação WEB com Flask e persistência JSON, vamos criar uma aplicação para de organização de tarefas, em que uma tarefa é cadastrada  com seu nome e status, sendo o status escolhido entre: "a fazer", "em andamento" ou "concluída".

A estrutura da aplicação deve seguir o MVC, assim temos o diretório do PROJETO, e as subdivisões: templates (para as VIEW), models (funções com a logica de negócio e acesso aos dados), controllers (rotas que fazem a ligação da VIEW e lógica de negócios).

**templates** - aqui criaremos os arquivos: `base.html`, `index.html`, `add.html` e `edit.html`, para interação no navegador e apresentação de resultados.

**models** - aqui teremos um diretório **data**, que armazena o arquivo `dados.json` com os dados cadastrados de cada tarefa.

**controllers** - aqui organizamos o `front_controller.py`, um arquivo que gerencia as rotas e faz a comunicação entre VIEW e MODEL.

**static** - iremos criar um diretório para guardar imagens que colocaremos nos botões, para melhorar a interface, mas caso prefira usar os ícones do Bootstrap, não esqueça de colocar o link de acesso aos ícones no `base.html`. O diretório deve ser criado com o nome **image**. O diretório **css** também é criado em **static**. Caso faça upload de arquivos, eles também ficam nesse diretório, dentro do subdiretório **uploads** - essa recomendação é do Flask, para acessos externos.

Diretamente no PROJETO, criaremos o arquivo `app.py`, que em grandes sistemas pode ser trocado pelo `__init__.py`. Iremos manter o `app.py`. Neste mesmo local criaremos o arquivo `config.py` com as definições mais gerais, como os caminhos para acessar o arquivo JSON. Também criaremos um arquivo `requirements.txt`, para anotarmos os requisitos necessários para a execução do aplicativo (também pode conter uma breve descrição da aplicação).


Não se esqueça de criar o ambiente virtual, ativá-lo, intalar o Flask e executar as configurações iniciais.

______________________________________________________________________________

---

<!-- Fonte: roteiro2.md -->

# Aula 14 - Padrão MVC para Projetos com Flask e JSON 
## Uso do CRUD To...DO

**Roteiro 2. ARQUIVOS BASE, CONFIG e APP**

Vamos organizar os arquivos gerais do projeto: `app.py`, `config.py` e `base.html`. Esses arquivos são os iniciais para dar suporte ao projeto. Aqui já usaremos **BLUEPRINT** para organizar as rotas de acesso.

Primeiro o `base.html`. As formatações comuns para todas as VIEW ficarão aqui (uso do **BLOCK**), incluindo as mensagens `FLASH`. Observe que os links Bootstrap para formatações e ícones já estão inseridos.

`base.html`

```html
<!DOCTYPE html>
<html lang="PT-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exemplo de Uso Padrão MVC</title>
       
    <!--LINK Para usar o BOOTSTRAP -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">    
    
    <!--LINK para ícones do BOOTSTRAP -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.css" integrity="sha384-Bk5cbLkZQ5raZ0+H2/+VbfYx3WpvxvQK4zqXZr7sYODuaX7bKXoSOnipQxkaS8sv" crossorigin="anonymous">
</head>

<body class="d-flex flex-column min-vh-100">   

    <!-- Apresentação das Mensagens FLASH -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
            <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                {{ message }}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <h3 class="text-center">Exemplo de Uso - Padrão MVC</h3>
    <hr><br>

    <div class="container-fluid">
        {% block conteudo %}

        {% endblock conteudo %}
    </div>
    
    <footer class="footer mt-auto py-3 bg-light">
        <div class="container text-center">
            <p class="mb-0">Uso do Padrão MVC - ARQAWB1 - 2026</p>
        </div>
    </footer>

    <!--JavaScriptBundle Para usar o BOOTSTRAP-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
</html>
```

O arquivo `config.py` contém as configurações e definições gerais e usaremos para definir os caminhos do arquivo JSON, em relação ao `app.py`. O uso de definições (constantes) é altamente recomendado, visto que aplicações Web são grandes e separadas em módulos (gerenciadas por vários BLUEPRINT e por vários desenvolvedores).


`config.py`

```python
import os

#Definições para acesso aos diretórios que armazenam o arquivo JSON

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "models", "data", "dados.json")

``` 

O arquivo `app.py` é o que inicializa a aplicação. No MVC ele é responsável ou por apresentar a VIEW de abertura ou importar e registrar o(s) **Blueprint** com o controller do projeto que fará a comunicação entre VIEW e MODEL.

Para o projeto, como a VIEW inicial já apresenta dados das tarefas cadastradas, vamos apenas fazer o registro do **Blueprint**, que será criado nos próximos passos. E como usaremos mensagens flash para o feedback, precisamos da **secret_key**, usada também quando temos o uso de seções. Lembrando que nossa aplicação da Lista de Tarefas possui apenas uma funcionalidade (CRUD para tarefas), assim, vamor criar e registrar apenas um **Blueprint**.

Ainda, como o `app.py` não necessita de funções das bibliotecas de forma direta, as bibliotecas serão importadas no arquivo que irá usar as funções, na aplicação, faremos a importação no arquivo `tarefa_controller.py`.


`app.py`

```python

from flask import Flask

#Aqui estamos importando tudo que o tarefa_bp cria e define: rotas de acesso e funções. Atenção ao caminho.
from controllers.tarefa_controller import tarefa_bp

app = Flask(__name__)

#Uso de sessões e mensagens FLASH
app.secret_key = 'chaveAWB1'

# Registra o Blueprint que foi criado para as funcionalidades de Tarefa
app.register_blueprint(tarefa_bp)

if __name__ == '__main__':
    app.run(debug=True)

```

O registro do Blueprint no `app.py` serve para modularizar a aplicação Flask. Ele permite que diferentes partes da aplicação sejam organizadas em componentes menores e independentes, facilitando a manutenção, escalabilidade e reutilização do código.

A importação e criação do Blueprint será feita no **controller**, para deixar mais modular e de acordo com o padrão MVC.

O arquivo `tarefa_controller.py` contém um Blueprint definido para agrupar rotas, handlers e outras funcionalidades relacionadas. Assim, quando registramos o Blueprint, estamos integrando o conteúdo do `tarefa_controller` com a aplicação principal. Todas as rotas e funcionalidades definidas no `tarefa_controller` passam a ser reconhecidas pela aplicação Flask.

Agora temos os arquivos de suporte ao projeto definidos.
______________________________________________________________________________

---

<!-- Fonte: roteiro3.md -->

# Aula 14 - Padrão MVC para Projetos com Flask e JSON 
## Uso do CRUD To...DO

**Roteiro 3. VIEW inicial e VIEW para adicionar novas tarefas**

VIEW `index.html`: aqui temos duas partes: o cadastro de novas tarefas e a vizualização das tarefas já cadastradas e gravadas no arquivo `dados.json`, que aparecem divididas de acordo com o statua da tarefa.

**Vamos organizar primeiro a parte do cadastro.**

Para cadastrar uma nova tarefa temos um botão que aciona a rota `@add`, que agora será gerenciada pelo `tarefa_controller`. Assim o acesso a essa e todas as rotas deve indicar o controller que está sendo utilizado.

Aqui temos página principal, que permite cadastrar e vizualizar as tarefas.

`index.html`

```html

{% extends 'base.html' %}

{% block conteudo %}
    
    <!-- Adicionar nova tarefa -->
    <div class="d-flex justify-content-between mb-3">
        <form action="{{ url_for('tarefas.add') }}" method="GET">
            <button type="submit" class="btn btn-primary d-flex align-items-center">
                <img src="{{ url_for('static', filename='image/add.png') }}" alt="Ícone" style="width: 20px; height: 20px; margin-right: 5px;">
                Adicionar Tarefa
            </button>
        </form>
        <br>       
    </div>

{% endblock conteudo%}

```

O método do formulário foi colocado como `GET`, porque nenhum dado é passado para a rota. O que se deseja é que a rota **renderize** a VIEW de cadastro de uma nova tarefa.

Observe que o botão "Adicionar Tarefa" tem uma imagem. Essa imagem deve ser colocada no caminho indicado e acessada com `url_for`. Neste exemplo o caminho completo é: **pasta_do_projeto->static->image->nome_imagem** . Lembre-se que `url_for` sempre inicia a partir do local do `app.py`. Mas você pode utilizar um ícone do Bootstrap, a escolha é sua.

Vamos criar o formulário para o cadastro das tarefas. Chamaremos esse arquivo de `add.html`, para ficar intuítivo e ter correspondência com a rota de ação.

`add.html`

```html

{% extends 'base.html' %}

{% block conteudo %}
    <h2>Adicionar Nova Tarefa</h2>
    <form method="POST" class="mt-3" action="{{url_for('tarefas.add')}}">
        <div class="mb-3">
            <label for="name" class="form-label">Nome da Tarefa</label>
            <input type="text" name="name" id="name" class="form-control" placeholder="Nome da Tarefa" required>
        </div>

        <div class="mb-3">
            <label for="status" class="form-label">Situação</label>
            <select name="status" id="status" class="form-select">
                <option value="a_fazer">A Fazer</option>
                <option value="em_andamento">Em Andamento</option>
                <option value="concluido">Concluído</option>
            </select>
        </div>

        <button type="submit" class="btn btn-sm btn-outline-success">Salvar Tarefa</button>
        <!-- Voltar sem realizar ação -->
        <a href="{{ url_for('tarefas.index') }}" class="btn btn-sm btn-outline-secondary ms-2">Voltar</a>
    </form> 
{% endblock conteudo %}

``` 
No cadastro da tarefa colocamos uma lista de seleção para escolher o status da tarefa e caso não seja escolhido um status, o "a fazer" foi colocado como valor default.

A VIEW ainda apresenta um botão para confirmar a ação (Salvar Tarefa) e um link para voltar para a VIEW anterior, sem concluir a ação. Ao se confirmar a ação, a `@rota add` é acionada, com o uso de indicação do `tarefa_controller`.

É nessa VIEW que os dados são efetivamente enviados para a `@rota add( )`, que os enviará para a função add( ) fazer a inserção no arquivo.
______________________________________________________________________________

---

<!-- Fonte: roteiro4.md -->

# Aula 14 - Padrão MVC para Projetos com Flask e JSON 
## Uso do CRUD To...DO

**Roteiro 4. VIEW inicial mostrar as tarefas**

VIEW `index.html`. Vizualização das tarefas na página principal, divididas por status: TO DO  --  DOING  --  DONE.

`index.html`

```html
{% block conteudo %}    
    <!-- Adicionar nova tarefa (feito no roteiro 1)-->
    
<!-- Vizualizar a Lista de Tarefas -->
    <table class="table table-bordered">
        <caption style="caption-side: top;"><strong>Tabela 1. Listagem de Tarefas</strong></caption>
        <thead>            
            <tr>
                <th>TO DO</th>
                <th>DOING</th>
                <th>DONE</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td>
                    {% for item in items %}
                        {% if item.status == 'a_fazer' %}
                            <div class="mb-2">
                                {{ item.name }}
                                <a href="{{ url_for('tarefas.edit', id=item.id) }}" class="btn btn-sm btn-outline-secondary">
                                    <img src="{{url_for('static', filename='image/edit.png')}}" alt="Ícone" style="width: 20px; height: 20px; margin-right: 5px;">
                                    Editar
                                </a>

                                <a href="{{ url_for('tarefas.delete', id=item.id) }}" class="btn btn-sm btn-outline-secondary" onclick="return confirm('Confirma exclusão da tarefa: {{item.name}} ?');">
                                    <img src="{{url_for('static', filename='image/del.png')}}" alt="Ícone" style="width: 20px; height: 20px; margin-right: 5px;">
                                    Apagar
                                </a>
                            </div>
                        {% endif %}
                    {% endfor %}
                </td>
                <td>
                    {% for item in items %} 
                        {% if item.status == 'em_andamento' %}
                        <div class="mb-2"> 
                            {{ item.name }} 
                            <a href="{{ url_for('tarefas.edit', id=item.id) }}" class="btn btn-sm btn-outline-secondary">
                                <img src="{{url_for('static', filename='image/edit.png')}}" alt="Ícone" style="width: 20px; height: 20px; margin-right: 5px;">
                                Editar
                            </a>

                            <a href="{{ url_for('tarefas.delete', id=item.id) }}" class="btn btn-sm btn-outline-secondary" onclick="return confirm('Confirma exclusão da tarefa: {{item.name}} ?');">
                                <img src="{{url_for('static', filename='image/del.png')}}" alt="Ícone" style="width: 20px; height: 20px; margin-right: 5px;">
                                Apagar
                            </a>
                        </div>
                        {% endif %}
                    {% endfor %}
                </td>
                <td>
                    {% for item in items %}
                        {% if item.status == 'concluido' %}
                        <div class="mb-2"> 
                            {{ item.name }}
                            <a href="{{ url_for('tarefas.edit', id=item.id) }}" class="btn btn-sm btn-outline-secondary">
                                <img src="{{url_for('static', filename='image/edit.png')}}" alt="Ícone" style="width: 20px; height: 20px; margin-right: 5px;">
                                Editar
                            </a>

                            <a href="{{ url_for('tarefas.delete', id=item.id) }}" class="btn btn-sm btn-outline-secondary" onclick="return confirm('Confirma exclusão da tarefa: {{item.name}} ?');">
                                <img src="{{url_for('static', filename='image/del.png')}}" alt="Ícone" style="width: 20px; height: 20px; margin-right: 5px;">
                                Apagar
                            </a>
                        </div>
                        {% endif %}
                    {% endfor %}
                </td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="3" style="font-size: small; text-align: right;"> Atualizado em: {{ data }} </td>
            </tr>
        </tfoot>
    </table>
{% endblock conteudo%}

```

4.1 Para selecionar onde colocar cada tarefa, foi construído um FOR dentro de cada coluna. Esse FOR percorre a lista e seleciona somente a tarefa de um status, para apresentar na coluna.

4.2 Já colocamos os botões para editar e apagar as tarefas, bem como as rotas associadas a cada ação. E para apagar uma tarefa, já adicionamos a confirmação da ação. Como já trabalhamos com esses conceitos no CRUD anterior, a explicação não está anotada aqui.

4.3 A edição de uma tarefa também precisa de uma VIEW. Vamos ver como fica o arquivo `edit.html` para editar uma tarefa. Observe que, na edição e exclusão, precisamos informar qual tarefa será editada ou apagada, assim, precisamos informar uma identificação da tarefa. Usamos o ID, criado automaticamente, no cadastro.


`edit.html`

```html
{% extends 'base.html' %}
{% block conteudo %}
    <h2>Editar Tarefa</h2>
    <form method="post" class="mt-3" action="{{url_for('tarefas.edit', id = item.id)}}">
        <div class="mb-3">
            <label for="name" class="form-label">Nome da Tarefa</label>
            <input type="text" name="name" id="name" class="form-control" value="{{ item.name }}" required>
        </div>

        <div class="mb-3">
            <label for="status" class="form-label">Situação</label>
            <select name="status" id="status" class="form-select">
                <option value="a_fazer" {% if item.status == 'a_fazer' %}selected{% endif %}>A Fazer</option>
                <option value="em_andamento" {% if item.status == 'em_andamento' %}selected{% endif %}>Em Andamento</option>
                <option value="concluido" {% if item.status == 'concluido' %}selected{% endif %}>Concluído</option>
            </select>
        </div>

        <button type="submit" class="btn btn-sm btn-outline-success">Salvar Alterações</button>
          <!-- Voltar sem ação -->
          <a href="{{ url_for('tarefas.index') }}" class="btn btn-sm btn-outline-secondary ms-2">Voltar</a>
    </form>    
{% endblock conteudo %}
```

A VIEW apresenta um botão para confirmar a ação e um link para voltar na VIEW anterior, sem concluir a ação. Ao se confirmar a ação, a `@rota edit` é acionada, com o uso de indicação do `tarefa_controller`.

______________________________________________________________________________

---

<!-- Fonte: roteiro5.md -->

# Aula 14 - Padrão MVC para Projetos com Flask e JSON 
## Uso do CRUD To...DO

**Roteiro 5. Funções com lógica de negócio e de acesso aos dados**


As operações que implementam a lógica de negócios, com acesso aos dados, fazem parte do **MODEL**.

Dentro do diretório **MODELS** temos um subdiretório **DATA**, onde colocamos o arquivo `JSON`. No **models** colocaremos o arquivo com as funções que implementam as operações. No projeto usaremos o arquivo `data_manager.py` para implementar essas funções. As funções que usaremos são para gravar dados no arquivo (C), ler e consultar dados do arquivo (R), alterar dados do arquivo (U) e excluir dados do arquivo (D), por isso o nome gerenciador de dados.

Observe que as funções são bem parecidas, quase iguais, às do CRUD anterior, porque estamos usando a mesma forma de armazenamento dos dados (`dados.json`). O uso de um Banco de Dados requer novas funções e novas formas de acesso, mas usando o MVC, as VIEW podem ser as mesmas.

`data_manage.py`

```python

import os
import json
import config

#-- FUNÇÕES PARA MANIPULAR O ARQUIVO: ler e gravar dados no arquivo

def load_data():
    if not os.path.exists(config.DATA_FILE):
        return [ ]
    with open(config.DATA_FILE, "r") as file:
        return (json.load(file))
        
def save_data(data):
    with open(config.DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


#-- FUNÇÕES PARA MANIPULAR cada registro do ARQUIVO

#retorna todos os itens armazenados ou vazio, caso o arquivo esteja vazio.
def recuperaTodos():
    return (load_data( ))

#retorna um item específico pelo ID ou vazio, caso não encontre.
def busca_item(item_id):
    items = load_data()
    return next((item for item in items if item['id'] == item_id), None)

#adiciona uma nova tarefa com base nos dados do formulário (parâmetro).
def add_item(form_data):
    name = form_data.get('name')
    status = form_data.get('status', 'a_fazer')  # Valor default, caso esteja em branco: 'a_fazer'
    
    if not name:
        return (False)
    
    #Lista com todas as tarefas cadastradas e que receberá o append( ) com a nova tarefa
    items = load_data( )
    
    #cria um ID automático - próximo valor inteiro a partir da última tarefa cadastrada
    new_id = max([item['id'] for item in items], default=0) + 1
    
    novo_item = {"id": new_id, "name": name, "status": status}
    items.append(novo_item)
    save_data(items)
    return (True)

#altera (atualiza) um item existente.
def altera_item(item_id, form_data):
    items = load_data()
    item = next((i for i in items if i['id'] == item_id), None)
    if (item):
        item['name'] = form_data.get('name')
        item['status'] = form_data.get('status', item['status'])  # Atualiza o status
        save_data(items)
        return True
    return False

#remove um item pelo ID.
def apaga_item(item_id):
    items = load_data()
    altera_items = [item for item in items if item['id'] != item_id]
    save_data(altera_items)
    return True


```

Nesse projeto as funções foram divididas em funções de acesso ao arquivo (leitura e escrita) e funções que acessam os registros amazenados no aruivo. No projeto CRUD anterior, essa lógica de negócio estava implementada diretamente em cada `@rota`, sem separação e isso dificulta manutenção e reuso de funções.

As funções que manipulam arquivos são as mesmas do CRUD anterior, da agenda de contatos.

______________________________________________________________________________

---

<!-- Fonte: roteiro6.md -->

# Aula 14 - Padrão MVC para Projetos com Flask e JSON 
## Uso do CRUD To...DO

**Roteiro 6. CONTROLLER**

As rotas e seus acessos e permissões são gerenciadas pelo **CONTROLLER**. 
Toda a comunicação entre VIEW e MODEL deve passar pelo CONTROLLER, que organiza os acessos e trocas de mensagens.

O arquivo `front_controller.py` possui todas as rotas, que chamam as funções do `data_manager.py` conforme o que é recebido da VIEW ou conforme o que deve ser retornado para a VIEW.

```python

from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint

from datetime import datetime


# Cria um Blueprint para as rotas
tarefa_bp = Blueprint('tarefas', __name__)
# Blueprint (tarefa_bp) no controlador (tarefa_controller.py) é um módulo que agrupa as rotas com as funções.
# O Flask precisa saber que o tarefa_controller existe - registra o controlador no APP.PY.


#-- importando todas as funções do data_manager.py
from models.data_manager import recuperaTodos, add_item, busca_item, altera_item, apaga_item


#-- rota principal
@tarefa_bp.route('/')
def index():
    items = recuperaTodos()
    data = datetime.now( ).strftime("%d/%m/%Y")
    return (render_template('index.html', items = items, data = data))

#-- rota para adicionar um registro (tarefa) no arquivo
@tarefa_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        resultado = add_item(request.form) #Parâmetro contém todos os campos do formulário
        if (not resultado):
            flash("É necessário colocar o nome da tarefa", "danger")
        else:
            flash("Tarefa adicionada com sucesso!", "success")
            return redirect(url_for('tarefas.index'))   
    return render_template('add.html')

#-- rota para alterar um registro (tarefa) específico no arquivo
@tarefa_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = busca_item(id)
    if not item:
        flash("Tarefa não encontrada para edição", "danger")
        return redirect(url_for('tarefas.index'))
    if request.method == 'POST':
        if altera_item(id, request.form):
            flash("Tarefa alterada com sucesso", "success")
            return redirect(url_for('tarefas.index'))    
    return render_template('edit.html', item=item)

#-- rota para excluir um registro (tarefa) específico no arquivo
@tarefa_bp.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    item = busca_item(id)
    if not item:
        flash("Tarefa não encontrada para exclusão", "danger")
        return redirect(url_for('tarefas.index'))
    apaga_item(id)
    flash("Tarefa excluída com sucesso", "success")
    return redirect(url_for('tarefas.index'))


``` 

Observe que agora as rotas são ativadas pelo BLUEPRINT `tarefa_bp` e devem indicar no cabeçalho da rota essa informação:

`@tarefa_bp.route('/)`

Pode parecer mais trabalhoso, mas a organização é necessária para separarmos: **lógica de negócios, dados e lógica de apresentação**. Assim, alterações, melhorias ou até mesmo correções ficam mais simples e organizadas. 

______________________________________________________________________________

### Claro que para projetos pequenos, o trabalho de implememtar tudo separado com o padrão MVC é exaustivo, até mesmo desnecessário. Mas somos aprendizes e vamos treinar para os grandes projetos que virão!

______________________________________________________________________________

