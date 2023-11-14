from flask import Flask, render_template, request
from psycopg import connect, OperationalError
from sys import exit


app = Flask(__name__)

database_config = {'host': 'localhost',
                   'dbname': 'postgres',
                   'user': 'postgres',
                   'password': '1234',
                   'port': '5432'}


def get_database_connection(database_config):
    # Try to connect with credentials to the database
    try:
        return connect(**database_config)
    except OperationalError as e:
        print(f'ERROR: Unable to connect to the database. {e}')
        return None
        

def insert_film_to_database(connection_obj, title: str, director: str,
                            release_year: int, country: str, my_rating: int,
                            short: bool):
    # Create a cursor to execute PostgreSQL commands in a database session
    cursor = connection_obj.cursor()
    # Create a table called 'films' (if it does not exist already)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS films (
            title TEXT,
            director TEXT,
            releaseYear INT,
            country TEXT,
            myRating REAL,
            short BOOLEAN
        );
    """)
    # Insert the new film data to the table
    cursor.execute(f"""
        INSERT INTO films (title, director, releaseyear, country,
myrating, short) VALUES ('{title}', '{director}', {release_year}, '{country}',
{my_rating}, {short})""")
    # Commit the pending transactions to the database
    connection_obj.commit()
    # Close cursor and connection object
    cursor.close()
    connection_obj.close()


@app.route('/movie_entry', methods=['GET', 'POST'])
def enter_movie():

    if request.method == "POST":
        try:
            title = request.form.get('title')
            director = request.form.get('director')
            release_year = request.form.get('releaseYear')
            country = request.form.get('country')
            my_rating = request.form.get('myRating')
            short = True if request.form.get('short') == 'on' else False
            print(title, director, release_year, country, my_rating, short)
        except KeyError:
            print('Make sure the field exists.')
        connection_object = get_database_connection(database_config)
        if connection_object is None:
            exit(0)
        insert_film_to_database(connection_object, title, director,
                                release_year, country, my_rating, short)
    return render_template('homepage.html')

