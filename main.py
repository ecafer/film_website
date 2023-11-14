from psycopg import connect, OperationalError
from sys import exit

# Try to connect with credentials to the database
try:
    connection_object = connect(host='localhost',
                                dbname="postgres",
                                user="postgres",
                                password="1234",
                                port=5432)
except OperationalError:
    exit('ERROR: Unable to connect to the database')

# Create a cursor to execute PostgreSQ command in a database session
cursor = connection_object.cursor()

# TBD: Do some database operations (in SQL)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS film (
        titel TEXT,
        director TEXT,
        releaseYear INT,
        country TEXT,
        myRating REAL,
        short BOOLEAN
    );
""")

# Commit the pending transactions to the database
connection_object.commit()
cursor.close()
connection_object.close()