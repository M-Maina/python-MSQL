import mysql.connector
con = mysql.connector.connect(host='localhost', database='school', user='root', password='Tronic@123')

cur = con.cursor()

cur.execute("DELETE FROM employee WHERE FIRST_NAME='Hassan' ")

con.commit()

print('Deleted Successfully')

