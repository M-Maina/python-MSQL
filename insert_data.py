import mysql.connector

#create a connection to the database
con = mysql.connector.connect(host='localhost', database='school', user='root', password='Tronic@123')
cur = con.cursor()

sql = "INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME,AGE,SEX,INCOME)"\
       "VALUES('Mahmoud', 'Ahmed', 20, 'M', 1000),\
              ( 'Amal', 'Mahmoud', 22, 'F', 800),\
              ('Hassan', 'Mohamed', 20, 'M', 5000)"
           
    

#create a cursor
cur.execute(sql)

#commit the query to the database
con.commit()

#execute query
con.close()
cur.close()

#print a statement
print('Data Inserted Succesfully')