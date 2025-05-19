# KeyMechService

Backend rest service for KeyMech app

## Develop

Fill local in the root project directory .env file.

POSTGRES_DB - name of the database

POSTGRES_USER - database username

POSTGRES_PASSWORD - database password

POSTGRES_HOST=postgres (Postgres container name)
    

Launch in development mode in watch mode over source code changes 

`docker compose up --watch`

To populate the database with data, launch project and run the filler python script from the ./dbfiller directory.

`python3 dbfiller/filler.py`

### Used containers


### postgres

Port 5432

Postgresql database container

Stores data externally at ./postgres/data

Uses sql init script at ./postgres/init if data directory is empty


### restapi

Port 8000

Main FastAPI container built from ./rest directory

Provides a REST API for consumers

Retrieves data from the database by accessing the **postgres** container


### media

Port 8080

Media FastAPI container build from ./media directory

Provides api call for retrieving an image by name

The image folder is mounted into the container directory /var/lib/media/images from the ./images directory
