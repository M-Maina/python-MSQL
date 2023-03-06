import mysql.connector
con = mysql.connector.connect(host='localhost', database='school', user='root', password='Tronic@123')

cur = con.cursor()

cur.execute("UPDATE employee SET AGE=20 WHERE FIRST_NAME='Amal' ")

con.commit()

print('Updated Successfully')