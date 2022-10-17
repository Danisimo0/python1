import pyodbc

def start(name, pyodbs=None):
    connection_str = 'DRIVER={Devart ODBC Driver for PostgreSQL};' \
                     'Server=postgres;' \
                     'Port=5432;' \
                     'Database=mydatabase;' \
                     'User ID=myuserid' \
                     'Password=mypassword' \
                     'String Types=Unicode' \

    connection = pyodbs.connect(connection_str)
    cursor = connection.cursor()
    connection.autocommit = False