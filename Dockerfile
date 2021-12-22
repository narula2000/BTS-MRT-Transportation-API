FROM python:3.8

RUN pip install pipenv

WORKDIR /code

COPY Pipfile* /code/

RUN pipenv lock --keep-outdated --requirements > requirements.txt

RUN pip install -r requirements.txt

COPY . /code/
