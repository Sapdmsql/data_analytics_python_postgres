# Python with PostgreSQL example

### Setup

1. Change content of the '.env' file with database credentials, e.g.:

FLASK_DEBUG=True
DBNAME=mydb
DBHOST=localhost
DBUSER=admin
DBPASS=geheim

2. Run the migrations:

    ```shell
    python3 -m flask db upgrade
    ```

### Run the example

Run the Jupyter notebook 'jupyter_postgres_db.ipynb'

