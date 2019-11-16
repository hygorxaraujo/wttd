# Eventex

Eventex project for the Welcome to the Django course.

## Dependencies

1. [Python 3.8](https://www.python.org/downloads/)
2. [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
3. [Docker](https://docs.docker.com/v17.12/install/)
4. [docker-compose](https://docs.docker.com/compose/install/)

## Setup

```bash
$ pipenv install --dev
```

## Running

- Start: `pipenv run up`
- Access: [http://localhost/](http://localhost/)
- Stop: `pipenv run down`
- Test (start first): `pipenv run tests` 

## Deploy

Automatic deploy to Heroku on [https://eventex-hygor.herokuapp.com/](https://eventex-hygor.herokuapp.com/) after each commit to `master`.
