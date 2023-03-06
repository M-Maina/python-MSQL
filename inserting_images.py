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


#YOU CAN ALSO TRY THIS CODE


import mysql.connector

cnx = mysql.connector.connect(user='root', password='yourpassword',
                               host='localhost', database='yourdatabase')
cursor = cnx.cursor()

with open('image.jpg', 'rb') as f:
    image_data = f.read()

add_image = ("INSERT INTO Images "
             "(ID, DATA) "
             "VALUES (%s, %s)")
image_id = 1  # Replace with the ID of the image
image_blob = mysql.connector.Binary(image_data)
data = (image_id, image_blob)

cursor.execute(add_image, data)
cnx.commit()

cursor.close()
cnx.close()
