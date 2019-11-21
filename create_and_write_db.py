import pyodbc
import pandas

cnx = pyodbc.connect(
        'Driver=IBM i Access ODBC Driver; '
        'System=p1214-pvm1.cecc.ihost.com; '
        'UserID=user1214; '
        'Password=z8ks0%uB-87o0Nk;'
        )
SCHEMA="example_s"

cursor = cnx.cursor()
sql = "create schema {}".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "set schema {}".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "CREATE TABLE {}.tmp(col1 INT, col2 INT, PRIMARY KEY(col1))".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "INSERT INTO {}.tmp (col1, col2) VALUES ( 1, 2)".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "INSERT INTO {}.tmp (col1, col2) VALUES ( 9, 2)".format(SCHEMA)
cursor.execute(sql)
cursor.commit()
