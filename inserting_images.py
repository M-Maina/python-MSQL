''' First go to the mysql commsnd client, USE <Database_Name> the create the table: CREATE TABLE Images (
    ID INT PRIMARY KEY,
    DATA MEDIUMBLOB
);
'''

import mysql.connector
con = mysql.connector.connect(host='localhost', database='school', user='root', password='Tronic@123')
photo = open('photo.png')
show_photo = photo.read()

cur = con.cursor()

cur.execute("INSERT INTO Images VALUES(1, %s)", (show_photo,))

con.commit()
print('Image Inserted successfully')