# Livro de Receitas :book:



## Detalhes do projeto



### Estrutura do projeto

O projeto está dividido em módulos, esta decisão foi tomada para separar as regras de negócio em diferentes ambientes, e isso possibilita que futuramente sejam incorporadas novas funcionalidades sem necessidade de refatorar todo o código.

- **livro_de_receitas** - Pacote principal do projeto
- **receitas** - Módulo responsável pelo gerenciamento dos models e do banco de dados.
- **chef** - Módulo responsável por gerenciar o acesso dos chefs: listagem, criação, alteração e exclusão de receitas.
- **client** - Módulo responsável por gerenciar o acesso dos clientes: listagem de receitas, busca e filtro.

<hr>



## Configurando o ambiente:



### Criação de ambiente virtual

É recomendado a criação de um ambiente virtual portanto, crie um ambiente virtual com `venv` ou `virtualenv` e ative-o:

Usando o `venv`

```bash
python3 -m venv tutorial-env
```

No Windows, execute:

```bash
tutorial-env\Scripts\activate.bat
```

No Unix ou no MacOS, execute:

```bash
source tutorial-env/bin/activate
```

Ou usando o `virtualenv`

```bash
virtualenv tutorial-env
```

No Unix ou no MacOS, execute:

```bash
. tutorial-env/bin/activate
```



### Instalação de dependências

Instale as seguintes bibliotecas

``` bash
pip install django
pip install djangorestframework
pip install django-filter
```



### Execute o servidor

Na pasta raiz do projeto, onde está o arquivo `manage.py` execute:

```bash
python manage.py runserver
```

Se tudo correr bem você verá:

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 12:07:08
Django version 3.2.9, using settings 'livro_de_receitas.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```



### Montando o banco de dados

Antes de criarmos o administrador e cadastrar os chefs e as receitas precisamos montar as tabelas do nosso banco de dados.

Encerre o servidor com `ctrl + c` e execute:

```bash
python manage.py makemigrations
```

E depois:

```bash
python manage.py migrate
```



### Criação de administrador

Com as tabelas do nosso banco de dados preparadas vamos criar um superusuário para cadastrar nossos chefs.

Para cadastrar um administrador do nosso projeto execute:

```bash
python manage.py createsuperuser --email admin@receitas.com --username admin
```

Insira uma senha e repita-a.

> Podemos alterar o email e o nome do administrador alterando os parâmetros --email admin@receitas.com --username admin
>
> Também é possível criar mais de um administrador.



### Execute o servidor novamente

Na pasta raiz do projeto, onde está o arquivo `manage.py` execute:

```bash
python manage.py runserver
```

Você verá:

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2021 - 12:07:08
Django version 3.2.9, using settings 'livro_de_receitas.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

Agora acesse http://127.0.0.1:8000/ em seu navegador.

Para acessar o painel administrativo vá para http://127.0.0.1:8000/admin/ e insira as credenciais que acabamos de criar.



## Testando a API através do navegador:

> Apesar de estarmos usando o navegador podemos também acessar todos os métodos da API abaixo usando o `postman` ou outra ferramenta de sua preferência.

### Cadastrando chefs

No painel administrativo ao lado de `Chef models` clique em `Adicionar`, insira um nome para o chef e clique em salvar.



### Cadastrando receitas - módulo chef

Com o chef cadastrado podemos agora criar receitas, para isso acesse a o módulo chef da API em http://127.0.0.1:8000/chef/

Selecione o chef e insira a receita no campo `Receita` e clique em `POST`



### Editando e excluindo receitas - módulo chef

Para editar uma receita coloque o número da `'id'` da receita na URL(/chef/1/), isto vai te direcionar para uma página de
detalhes onde será possível editar ou excluir a receita.

Para deletar clique em `DELETE`e confirme.

Para editar a receita altere o conteudo da receita e clique em `PUT`



### Listando receitas - módulo client

Para um cliente ter acesso às receitas a URL é http://127.0.0.1:8000/client/

Aqui podemos ver todas as receitas criadas.



### Filtrando receitas por chef - módulo client

Clique em `Filtros` lá podemos filtrar por chef em filtros, lá tem uma lista dos chefs.

http://127.0.0.1:8000/client/?chef=1 > Irá exibir apenas as receitas cadastradas pelo chef '1'.



### Buscando receitas por texto - módulo client

Clique em `Filtros` lá podemos realizar uma busca usando o campo de busca.

http://127.0.0.1:8000/client/client/?search=queijo > Irá exibir apenas as receitas que contiverem 'queijo' no texto da receita.



### Mesclando busca com filtro

Tanto a busca quanto o filtro pode ser feito diretamente através da URL, sendo possível mesclar os dois recurssos ex:

http://127.0.0.1:8000/client/client/?chef=1 > Irá exibir apenas as receitas cadastradas pelo chef '1'.

http://127.0.0.1:8000/client/client/?search=queijo > Irá exibir apenas as receitas que contiverem 'queijo' no texto da receita.

http://127.0.0.1:8000/client/client/?chef=1&search=queijo > Irá exibir apenas as receitas cadastradas pelo chef '1' e apenas aquelas que contiverem 'queijo' no texto da receita



<hr>

## Testes unitários

É possível rodar testes para verificar a integridade do projeto executando o comando:

```bash
python manage.py test
```

Este irá executar todos os testes, se desejar testar os módulos individualmente use:

Testar o módulo chef:

```bash
python manage.py test chef
```

Testar o módulo client:

```bash
python manage.py test client
```







