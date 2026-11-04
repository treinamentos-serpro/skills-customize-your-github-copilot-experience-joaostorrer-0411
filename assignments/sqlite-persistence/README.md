# 📘 Atividade: Persistência de Dados com SQLite

## 🎯 Objetivo

Aprenda a armazenar dados de forma persistente usando o módulo `sqlite3` do Python. Você criará um pequeno catálogo de livros capaz de manter seus dados mesmo depois que o programa for encerrado.

## 📝 Tarefas

### 🛠️ Criar o Banco de Dados e a Tabela de Livros

#### Descrição
Escreva um programa que crie ou abra um banco de dados SQLite chamado `books.db` e prepare uma tabela para armazenar livros.

#### Requisitos
O programa concluído deve:

- Conectar-se ao banco usando o módulo `sqlite3`, sem instalar bibliotecas externas
- Criar uma tabela `books` com `id`, `title` e `author`; o identificador deve ser único e gerado automaticamente
- Inserir pelo menos dois livros de exemplo e consultar os registros para confirmar que foram salvos
- Confirmar as alterações com `commit()` e encerrar a conexão

### 🛠️ Adicionar e Listar Livros

#### Descrição
Expanda o programa para permitir que a pessoa usuária adicione livros e consulte o catálogo. Use comandos SQL parametrizados para inserir os dados.

#### Requisitos
O programa concluído deve:

- Solicitar título e autor e inserir um novo livro na tabela
- Usar placeholders (`?`) e valores separados na consulta SQL, em vez de montar o comando com concatenação de strings
- Listar todos os livros com seus identificadores, títulos e autores
- Manter os livros existentes ao executar o programa novamente

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete o catálogo com opções para atualizar ou remover um livro pelo seu identificador. Teste as operações usando registros que já estejam salvos no banco.

#### Requisitos
O programa concluído deve:

- Atualizar o título e o autor do livro escolhido
- Remover o livro escolhido sem afetar os outros registros
- Informar quando o identificador informado não corresponde a nenhum livro
- Confirmar as alterações e permitir verificar o resultado listando o catálogo novamente
