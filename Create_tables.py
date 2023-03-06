import mysql.connector

con = mysql.connector.connect(host='localhost', database='school', user='root', password='your_password>')

cur =con.cursor()

sql = """CREATE TABLE EMPLOYEE (
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20) NOT NULL,
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT )"""
    
cur.execute(sql)
con.close()
print('Database Table Created Successfully')