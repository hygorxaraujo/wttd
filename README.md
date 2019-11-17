# Eventex

Eventex project for the Welcome to the Django course.

[![Build Status](https://travis-ci.org/hygorxaraujo/wttd.svg?branch=master)](https://travis-ci.org/hygorxaraujo/wttd)
[![Maintainability](https://api.codeclimate.com/v1/badges/95cd755c89262bfcac7e/maintainability)](https://codeclimate.com/github/hygorxaraujo/wttd/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/95cd755c89262bfcac7e/test_coverage)](https://codeclimate.com/github/hygorxaraujo/wttd/test_coverage)

## Develop

### Dependencies

1. [Python 3.8](https://www.python.org/downloads/)
2. [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
3. [Docker](https://docs.docker.com/v17.12/install/)
4. [docker-compose](https://docs.docker.com/compose/install/)

### Setup

1. Clone the repository
2. Create an environment with pipenv
3. Start a shell with the created environment
4. Configure the environment variables with the .env
5. Start the application
6. Run the tests

```console
git clone git@github.com:hygorxaraujo/wttd.git wttd
cd wttd
pipenv install --dev
pipenv shell
cp contrib/.env.template .env
pipenv run up
pipenv run tests
```

### Running

- Start: `pipenv run up`
- Access: [http://localhost/](http://localhost/)
- Stop: `pipenv run down`
- Test: `pipenv run tests` 

## Deploy
This repository is already configured with an automatic deploy.
After each commit to `master`, the deploy is started to Heroku on [https://eventex-hygor.herokuapp.com/](https://eventex-hygor.herokuapp.com/).

### Dependencies
1. [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

### Setup and deploy
1. Setup an instance in Heroku
2. Send configurations to Heroku
3. Define a safe SECRET_KEY for the instance
4. Define DEBUG=False
5. Define the stack as container
6. Configure the email service
7. Send the code to heroku

```console
heroku create myeventex
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
heroku stack:set container
# configure email
git push heroku master --force
```
