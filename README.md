# FastAPI_example
This project was created to practice technologys with:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Pytest](https://docs.pytest.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [poetry](https://python-poetry.org/)
- [Uvicorn](https://www.uvicorn.org/)

## Getting started

This document includes instructions to get the project running in development.

### Running the project locally

#### Pre-requisites:


- [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart-pt)
- [Python 3.8+](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-20-04-server-pt)
- [Poetry](https://python-poetry.org/docs/)


#### Guide

1. Open your terminal and change directory to the project's root:
   ```bash
   cd FastAPI_example
   ```

2. Copy the sample environment variables file and edit them to your environment:
   ```bash
   cp .env.sample .env
   ```
   * **SQLALCHEMY_DATABASE_URI** -> The URI that FastAPI example. will try to connect.
<br/><br/>

3. Spawn a shell with the virtualenv activated:
   ```bash
   poetry shell
   ```

4. Install all packages specified:
   ```bash
   poetry install
   ```

5. Run migration:
   ```bash
   poetry run alembic upgrade head
   ```

6. Run the tests:
   ```
   poetry run pytest
   ```

7. Run your project:
   ```bash
   poetry run uvicorn app.app:main --host localhost --port 8002
   ```

8. Documentation wiil be available by  accessing the API endpoint below:
   ```
   http://localhost:8002/docs
   ```