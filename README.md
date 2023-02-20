<div align="center" id="top">
  <!-- <img src="./.github/app.gif" alt="Limpa Bem Front" /> -->

  &#xa0;

  <a href="https://web-production-7067.up.railway.app/">Demo</a>
</div>

<h1 align="center">Limpa Bem Backend</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/AlissonAzevedo/limpa-bem?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/AlissonAzevedo/limpa-bem?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/AlissonAzevedo/limpa-bem?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/AlissonAzevedo/limpa-bem?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/limpa-bem?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/limpa-bem?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/limpa-bem?color=56BEB8" /> -->
</p>

<!-- Status -->

<h4 align="center">
	🚧  Limpa Bem Backend 🚀 Em construção...  🚧
</h4>

<hr>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0;
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/AlissonAzevedo/" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

A empresa LIMPA-BEM (de serviços de serviços de limpeza)
precisa fazer um acompanhamento e controle dos serviços
que eles tem oferecido, bem como disponibilizar para o
cliente poder agendar um serviço, no momento está tudo
sendo feito de maneira manual.

## :bulb: Proposta ##

O desafio consiste em implementar a solução que ajudaria
a empresa LIMPA-BEM usando as seguintes tecnologias:
* Python com django/django restframework (é
recomendado o uso do admin do django como
interface de uso do sistema)
* Banco de dados SQL (postgres, sqlite, mysql)
* HTML, CSS, javascript (se julgar necessário pode usar
um framework front-end)

```bash
https://web-production-7067.up.railway.app/
```

## :sparkles: Features ##

:heavy_check_mark: Endpoint de serviços realizados no dia\
:heavy_check_mark: CRUD agendamentos\
:heavy_check_mark: CRUD Clientes\
:heavy_check_mark: CRUD funcionários

## :rocket: Technologies ##

As seguintes ferramentas foram usadas neste projeto:

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [REST framework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Django CORSHEADRS](https://pypi.org/project/django-cors-headers/)
- [Jazzmin](https://django-jazzmin.readthedocs.io/)

## :white_check_mark: Requirements ##

Antes de iniciar :checkered_flag:, você precisa ter [Git](https://git-scm.com) e [Python](https://www.python.org/) instalados.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/AlissonAzevedo/limpa-bem

# Access
$ cd limpa-bem

#Create virtual ENV
$ python -m venv 'NameEnv'

# Activate VirtualEnv
$ 'NameEnv'\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Migrate
$ py manage.py migrate

# Create SuperUser
$ python manage.py createsuperuser

# Start server
$ py manage.py runserver

# The server will initialize in the <http://127.0.0.1:8000/>
```

## :memo: License ##

Este projeto está sob licença do MIT. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE.md).


Made with :heart: by <a href="https://github.com/AlissonAevedo/" target="_blank">Alisson Azevedo</a>

&#xa0;

<a href="#top">Back to top</a>
