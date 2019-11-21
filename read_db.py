import pyodbc
import pandas

cnx = pyodbc.connect(
        'Driver=IBM i Access ODBC Driver; '
        'System=p1214-pvm1.cecc.ihost.com; '
        'UserID=user1214; '
        'Password=z8ks0%uB-87o0Nk;'
        )
SCHEMA="example_s"
sql = "Select * from {}.tmp".format(SCHEMA)
data = pandas.read_sql(sql, cnx)
print(data)
