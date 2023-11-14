import psycopg

connection_object = psycopg.connect(host='localhost',
                                    dbname="postgres",
                                    user="postgres",
                                    password="1234",
                                    port=5432)

cursor = connection_object.cursor()

# TBD: Do some database operations


connection_object.commit()
cursor.close()
connection_object.clos()