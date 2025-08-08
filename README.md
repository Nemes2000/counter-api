# counter-api

This project is done for an interview. The specifcation was the following:

A program egy számlálót valósít meg, aminek az értékét adatbázisban tárolja, és API-n keresztül képes az
érték manipulálására. Három funkciót kell megvalósítani:
 -  A számláló jelenlegi értékének lekérése
 -  A számláló értékének növelése egy megadott pozitív értékkel
 -  A számláló értékének kinullázása
Az API endpoint definíciójára OpenApi leírót használj.

Az adatbázis kapcsolat paraméterei (host, port, felhasználónév, jelszó, adatbázisnév) környezeti
változókból legyenek beolvasva.

A program JSON formátumban válaszoljon a jelenlegi érték lekérdezésére. A másik két esetben elég ha
csak a megfelelő http státusz kód a válasz.

Unit tesztek:

- Megfelelő működés tesztelése az adatbázis réteg mockolásával
- Edge case-k tesztelése ahol releváns

## Project structure

- db-config: docker file and db init script
- src: code files for the counter api
- tests: unit test files

## API endpoints

### GET /

Get the counter value.

**response**

| Body parameter | Type     | Description          |
| :------------- | :------- | :------------------- |
| `value`        | `number` | Value of the counter |

### POST /

Update the counter value.

**request**

| Body parameter | Type     | Description                                         |
| :------------- | :------- | :-------------------------------------------------- |
| `value`        | `number` | **Required**. The value you want to set the counter |

### DELTE /

Clear the counter value.

**request and response**

| Body parameter | Type | Description |
| :------------- | :--- | :---------- |

## Used technologies

- python 3.12
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Flask OpenAPI3](https://luolingchun.github.io/flask-openapi3/v3.x/)
- [pydantic](https://docs.pydantic.dev/latest/)
- [black](https://black.readthedocs.io/en/stable/index.html)
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [psycopg](https://www.psycopg.org/psycopg3/docs/)
- [pytest](https://docs.pytest.org/en/stable/)

## Run project

The following commands are valid if you run them in the project root!

### Run API and DB together

With docker compose you can run the API and DB containers together.

```
docker-compose up --build
```

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

### Run mypy

To check I used strict typing run:<br>
(I only excluded flask_openapi3, cause I could not resolve that issue.)

```
mypy .
```

### Run tests

For run usit test you need to run this line of code:

```
pytest -v
```
