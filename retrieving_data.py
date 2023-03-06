import mysql.connector
con = mysql.connector.connect(host='localhost', database='school', user='root', password='Tronic@123')

cur = con.cursor()

#execute query
cur.execute("SELECT * FROM employee")


#FetchAll
rows = cur.fetchall()

#Loop to print out all the data
for row in rows:
    print(row)
    
#FetchOne
row = cur.fetchone()

for i in range(cur.rowcount):
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    
    
    #with conditions
cur.execute("SELECT * FROM employee WHERE FIRST_NAME='Amal' ")

row = cur.fetchone()

for i in range(cur.rowcount):
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    
    