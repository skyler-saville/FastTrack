# Made with FastAPI

## Python Version: 3.9

To get started run the following command:

```pip install -r requirements.txt```

To run the server, run:

```uvicorn app.main:app --reload```

Swagger interactive API can be found at:

``` localhost:8080/docs ```

## Docker-Compose

Added a docker-compose.yml, which is used to create a postgres database as well as a pgAdmin server

``` docker-compose up ```

Added a 'sample.env' file. Update the values to what you want and rename the file to '.env'

## pgAdmin can be accessed via '127.00.0.1:5050'

Just use the credentials located in your '.env' file to login

```docker volume rm choresapi_db```
Deletes the local persisted database
