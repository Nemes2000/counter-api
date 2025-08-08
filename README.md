# counter-api

## Used technologies

- python 3.12
- [Flask](!https://flask.palletsprojects.com/en/stable/)
- [Flask OpenAPI3](!https://luolingchun.github.io/flask-openapi3/v3.x/)
- [pydantic](!https://docs.pydantic.dev/latest/)
- [black](!https://black.readthedocs.io/en/stable/index.html) --> run : python -m black src
- [mypy](!https://mypy.readthedocs.io/en/stable/) ---> run: mypy src
- [psycopg](!https://www.psycopg.org/psycopg3/docs/)
- [pytest](!https://docs.pytest.org/en/stable/)

## Run project

The following commands are valid if you run them in the project root!

### Run database

```
docker build -t counter-db .

docker run --rm --name counter-db -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydb -p 5432:5432 counter-db
```

### Run API

I use anaconda for package management!

```
conda activate

pip install -r requirements.txt

python src/api.py
```

### Run tests

For running test you need to run this line of code:

```
pytest -v
```
