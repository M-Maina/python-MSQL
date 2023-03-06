import mysl.connector

#create a connection to the database
con = mysl.connector.connect(host='localhost', database='mysql', user='root', passwords='<your set password')

#create a cursor
cur = con.cursor()

#execute query
cur.execute('CREATE DATABASE school')

#print a statement
print('Database created successfully')