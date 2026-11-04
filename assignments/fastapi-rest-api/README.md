# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar livros usando FastAPI. Você praticará métodos HTTP, validação de dados com modelos Pydantic e respostas com códigos de status apropriados.

## 📝 Tasks

### 🛠️ Criar Rotas para Consultar Livros

#### Descrição
Use o código inicial para criar uma API que permita consultar todos os livros e buscar um livro pelo seu identificador. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn main:app --reload`. Use a interface em `http://127.0.0.1:8000/docs` para testar as rotas.

#### Requisitos
O programa concluído deve:

- Criar uma rota `GET /books` que retorne a lista de livros armazenados
- Criar uma rota `GET /books/{book_id}` que retorne o livro correspondente
- Retornar o código de status `404` quando o identificador solicitado não existir
- Usar o livro de exemplo fornecido no código inicial para testar as consultas

### 🛠️ Adicionar Livros com Validação

#### Descrição
Implemente a criação de livros. Use os modelos Pydantic do código inicial para validar os dados recebidos pela API.

#### Requisitos
O programa concluído deve:

- Criar uma rota `POST /books` que aceite `title`, `author` e `year`
- Validar que `year` seja maior que zero e que os campos obrigatórios estejam presentes
- Atribuir um identificador único ao novo livro e adicioná-lo ao armazenamento em memória
- Retornar o livro criado com o código de status `201`

### 🛠️ Completar as Operações CRUD

#### Descrição
Complete a API adicionando operações para atualizar e remover livros. Teste os casos de sucesso e de identificadores inexistentes pela interface `/docs`.

#### Requisitos
O programa concluído deve:

- Criar uma rota `PUT /books/{book_id}` para atualizar os dados de um livro existente
- Criar uma rota `DELETE /books/{book_id}` para remover um livro existente
- Retornar `404` ao tentar atualizar ou remover um livro inexistente
- Retornar o código de status `204` ao remover um livro com sucesso
