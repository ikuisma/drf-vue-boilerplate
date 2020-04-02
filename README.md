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

- [Pyenv](https://github.com/pyenv/pyenv) –  version management for Python.
- [Poetry](https://python-poetry.org/) – package and dependency management for Python.
- [Node + NPM](https://nodejs.org/en/) – runtime for frontend.
- [Docker](https://docs.docker.com/get-docker/) – container platform for running external dependencies.

Optional but recommended:

- [NVM](https://github.com/nvm-sh/nvm) – version management for Node.js


### Installing

A step by step series of examples that tell you how to get a development env running.

Some of the Python libraries used by the project have their own prerequisite installation steps. Refer to the project homepage for more detailed installation instructions for other systems.

#### Install [python-xmlsec](https://github.com/mehcode/python-xmlsec) dependencies

macOS Homebrew
```
brew install libxml2 libxmlsec1 pkg-config
```
Linux Debian
```
apt-get install libxml2-dev libxmlsec1-dev libxmlsec1-openssl
```
#### Install project

Next use the following OpenSSL command to generate keys for the SAML Service Provider into the certs directory:
```
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -nodes -days 900
```

In a separate terminal execute the following command at the root of this repository to spin up the containerized SAML IDP:

```
docker-compose up
```

Once the SAML IDP is running visit [http://localhost:8080/simplesaml/saml2/idp/metadata.php](http://localhost:8080/simplesaml/saml2/idp/metadata.php) and copy the `X509Certificate` key from the XML returned by the URL. Open `settings.py` and paste the key into the following object:

```
SOCIAL_AUTH_SAML_ENABLED_IDPS = {
    "simplesamlidp": {
        "x509cert": "", <= Paste copied X509 cert here
        ...
    }
}
```


Next, install dependencies for the backend by running the following command from the project root:

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

You should now be able to access the site at [http://localhost:8000](http://localhost:8000). You can login to the application by either by using application's login form with the superuser credentials you created earlier, or by using the SAML IDP which comes with the following pre-made users:

- username: `user1` password: `user1pass`
- username: `user2` password: `user2pass`

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