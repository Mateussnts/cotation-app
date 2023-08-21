Desenvolvimento FullStack

Aplicação com back-end e front-end separados, para listar cotações em tempo real (periodicamente atualizadas) de algumas moedas utilizando algumas APIs. A aplicação conta com uma tela simples de login para realizar autenticação e um dashboard onde serão mostrados as cotações.

## Tecnologias utilizadas
 
 - Angular
 - Django
 - MySQL Data Base
 - Jason Web Token

## Manual de execução Front-end

Após a clonagem do repositorio abra a pasta client-side na IDE de sua preferência.

1. Execute o comando abaixo para instalação dos modulos node do Angular.
   ```bash
   npm install
   ```
2. Execute o comando para rodar a aplicação Angular.
   ```bash
   ng serve
   ```
## Links Úteis

- [http://localhost:4200/login](http://localhost:4200/login)
- [http://localhost:4200/cadastro](http://localhost:4200/cadastro)
- [http://localhost:4200/dashboard](http://localhost:4200/dashboard)

![loginpic](https://user-images.githubusercontent.com/40031501/160313112-9dfe617f-a5eb-4f4e-8823-99d2a1d4d0f0.png)

## Manual de execução Back-end

Após a clonagem do repositorio abra a pasta client-side na IDE de sua preferência.

1. Execute o comando para rodar a aplicação Django.
   ```bash
   python manage.py runserver
   ```
## Links Úteis

- [http://127.0.0.1:8000/api/login](http://127.0.0.1:8000/api/login) POST
- [http://127.0.0.1:8000/api/register](http://127.0.0.1:8000/api/register) POST
- [http://127.0.0.1:8000/api/dashboard](http://127.0.0.1:8000/api/dashboard) GET
- [http://127.0.0.1:8000/api/logout](http://127.0.0.1:8000/api/logout)

![imagem_2022-03-27_230524](https://user-images.githubusercontent.com/40031501/160314310-2f8e3599-7c49-4c5f-86e3-14806cf11d5f.png)

## Implementação a ser corrigidas e finalizadas

- Integração Back & Front end.
- Layout responsivo.
