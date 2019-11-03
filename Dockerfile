FROM python:3.8-alpine

RUN adduser -D wttd
ENV APP_HOME=/home/wttd
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY eventex eventex
COPY manage.py entrypoint.sh ./
RUN chmod +x entrypoint.sh

RUN chown -R wttd:wttd ./
USER wttd

ENTRYPOINT ["/home/wttd/entrypoint.sh"]
