# Django/DRF/Vue/Webpack/SAML Boilerplate

Boilerplate code for a project with:
- Vue -frontend served by Django
- DRF backend API
- Django Webpack Loader for HMR
- SAML SSO authentication with Python Social Auth

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The recommended installation method requires the following:

- [Pyenv](https://github.com/pyenv/pyenv) –  version management for Python
- [Poetry](https://python-poetry.org/) – package and dependency management for Python
- [Node + NPM](https://nodejs.org/en/) – runtime for frontend.

Optional but recommended:

- [NVM](https://github.com/nvm-sh/nvm) – version management for Node.js


### Installing

A step by step series of examples that tell you how to get a development env running.

First install dependencies for the backend by running the following command from the project root:

```
poetry install
```

Then `cd` into the frontend repository `vue-frontend` and run the following command:

```
npm install
```

Enter the Python virtual environment shell from the project root:

```
poetry shell
```

In the venv shell execute the following command to run the database migrations:

```
python manage.py migrate
```

Then run the following command to create a new superuser for yourself:

```
python manage.py createsuperuser
```

And then run the following command to start the development server:

```
python manage.py runserver
```

In a separate shell `cd` into the frontend repository `vue-frontend` and run the following command:

```
npm run serve
```

You should now be able to access the site at [http://localhost:8000](http://localhost:8000).

## Running the tests

TBA

## Deployment

TBA

## Built With

* Django
* Django Rest Framework
* Vue
* Django Webpack Loader

## Versioning

TBA

## License

TBA

## Acknowledgments

TBA