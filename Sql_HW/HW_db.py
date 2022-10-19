

import pyodbc
conn = pyodbc.connect('Driver={SQLite3 ODBC Driver};'
                      'Server=PostgreSQL 14;'
                      'Database=new;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('''
 CREATE TABLE Books (
        PersonId INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        LastName  TEXT NOT NULL,
        Age INTEGER NULL,
        CreatedAt TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL

);

               ''')
conn.commit()
cursor.execute('''
                INSERT INTO Books (Id, title, author, price, pageCounts)
                VALUES
                (1,'Bob','Smith', 55, 5000$),
                (2, 'Jenny','Smith', 66, 2000$)
                ''')
conn.commit()
cursor.execute('SELECT * FROM PeopleInfo')
for row in cursor:
    print(row)

print("Database Table List Info: ")
for table_info in cursor.tables(tableType='TABLE'):
    print(table_info.table_name)
print("Database Table Data Info: ")
cursor.execute("SELECT * from user")
datas = cursor.fetchall()
for data in datas:
    print (data)
cursor.execute("UPDATE Books SET tele ='1-87654321' WHERE name='a'")
cursor.execute("DELETE FROM Books WHERE id='d'")
cursor.execute("DROP TABLE Books")
conn.close()
# Накидал на быструю руку, не проверяя