# Python with PostgreSQL example

### Setup

🎥 [Watch a screencast of deploying and re-deploying the app.](https://www.youtube.com/watch?v=r6Hnp9RXUpY)

1. Install the requirements:

    ```shell
    python3 -m pip install -r requirements.txt
    ```

2. Create an `.env` file using `.env.sample` as a guide. Set the value of `DBNAME` to the name of an existing database in your local PostgreSQL instance. Set the values of `DBHOST`, `DBUSER`, and `DBPASS` as appropriate for your local PostgreSQL instance.

3. Run the migrations:

    ```shell
    python3 -m flask db upgrade
    ```

### Run the example

Run the Jupyter notebook 'jupyter_postgres_db.ipynb'

