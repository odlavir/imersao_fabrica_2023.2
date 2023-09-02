# Projeto de Imersão a Fábrica de Softwares - UNIPÊ 2023.2.

## Desafio final - Movie Marker API.

Esta API foi projetada para auxiliar na criação aplicativos e serviços que envolvam o cadastro de usuários, gerenciamento de filmes e interações de usuários com os filmes, através comentários e avaliações.

## Tecnologias

- Python 3.11
- Django 4.2.4
- Django Rest Framework 3.14
- PostgreSQL 15

## Instalação

1. Instalar o Python 3.11.
2. Criar uma pasta no seu computador.
3. Com o git bash instalado no seu computador.
4. Utilize o comando `git clone https://github.com/odlavir/imersao_fabrica_2023.2`.
5. Instalar uma venv e em seguida ativa-la.
6. Abra o terminal e digite o comando: `pip install -r requirements.txt.`   ** Esse comando fará o download de todas as dependências do projeto **
7. Ter instalado o PostgreSQL.

## Recursos principais e suas endpoints

1. Usuários:
    - `POST /users`: Cadastrar um novo usuário.
    - `GET /users/{id}`: Obter informações de um usuário específico.
    - `PUT /users/{id}`: Atualizar informações de um usuário.
    - `DELETE /users/{id}`: Excluir um usuário.
    
2. Filmes:
    - `POST /filmes`: Cadastrar um novo filme.
    - `GET /filmes/{id}`: Obter informações sobre um filme específico.
    - `PUT /filmes/{id}`: Atualizar informações de um filme.
    - `DELETE /filmes/{id}`: Excluir um filme.

3. Comentários e Avaliações:
   - `POST /watched-movies`: Criar um comentário e uma avaliação, específicando o filme e usuário.
   - `GET /watched-movies/{id}`: Obter o comentário e avaliação específico.
   - `PUT /watched-movies/{id}`: Atualizar o comentário e avaliação específico.
   - `DELETE /watched-movies/{id}`: Excluir o comentário e avaliação específico.
  
4. Admin
   - `/admin`: Acesso ao painel do administrador.
  

   
