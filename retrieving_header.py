import mysql.connector
con = mysql.connector.connect(host='localhost', database='school', user='root', password='Tronic@123')

cur = con.cursor()

cur.execute("SELECT * FROM employee WHERE FIRST_NAME='Amal' ")

#fetch all data
row = cur.fetchone()

#column header
desc = cur.description
print(desc[0][0] , desc[1][0] , desc[2][0])
print('__________________________________')
for i in range(cur.rowcount):
    print(row[0], row[1], row[2] , row[3] , row[4])
