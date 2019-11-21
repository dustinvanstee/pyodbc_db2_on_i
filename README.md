# pyodbc_db2_on_i
A quick repo to show how to connect Python client to IBM i

This repo is intended do document one example of connecting to DB2 on IBM system i.  I had explored ibm_db but had a lot of licensing issues, we are are going to explore the pyodbc python package instead.

markdown exmpales
This site was built using [GitHub Pages](https://pages.github.com/)

- George Washington
- John Adams
- Thomas Jefferson
## My Environment
* client   : IBM Power8 VM, RHEL 7.6 with Anaconda3 : kernel 4.14.0-115.8.1.el7a.ppc64le
* database : IBM i 7.4 with DB2 on Power8

## Client Setup 
Here were the steps and links to setup my client machine.
I referenced this link that had some good information also [IBMI Open Source Software ODBC](https://github.com/IBM/ibmi-oss-examples/blob/master/odbc/odbc.md)



### Install Anaconda3 Python
Follow the directions here .. [Install Anaconda Python3](https://docs.anaconda.com/anaconda/install/linux-power8/)

### Install IBM i Access - Client Solutions
Note, you will need an IBMid to login.  If you haven't already done so, create one.

Follow the links here is install this software.  This software will be used by the pyodbc python package to connect to DB2 on i over ODBC.  It provides the proper drivers.

[Install IBM i Access - Client Solutions](https://www.ibm.com/support/pages/ibm-i-access-client-solutions)

click here -> ![Image description](images/download.png)

then sign in using your IBMid

Then select ACS for linux ![ACS](images/acs.png) and agree ![agree](agree.png)

### Configure ACS software

If you downloaded the right file, you should have a file name something like this *IBMiAccess_v1r1_LinuxAP.zip*

Now run these commands to install
```unzip IBMiAccess_v1r1_LinuxAP.zip
cd ppcle64
yum install ibm-iaccess-1.1.0.12-1.0.ppc64le.rpm
```

Once thats installed, you will need create a connection file in /etc/odbc.ini (or in $HOME/.odbc.ini) .  Here is the one I used ... 
cat /etc/odbc.ini

```[MYDSN]
Description=My IBM i System
Driver=IBM i Access for Linux ODBC Driver
System=*****.example.com
UserID=*******
Password=***********
```

Make special note of the name you selected in brackets.  This will be used in our python code.  Also note, your **driver string needs to match exactly one of the drivers in /etc/odbcinst.ini**  

```cat /etc/odbcinst.ini | grep -i driver```

Once you have your /etc/odbc.ini your all set, and ready to do some python!

### Python Setup
For python, I just needed to install pyodbc package
```pip install pyodbc```
and then experiment with creating a table, inserting some rows and reading it into pandas as a test.

I have 2 python files create_and_write_db.py and read_db.py.   These 2 files show some VERY BASIC commands but are enough to get you started ...


#### Create a table, and insert rows
```import pyodbc
import pandas

cnx = pyodbc.connect(
        'Driver=IBM i Access ODBC Driver; '
        'System=*****; '
        'UserID=******; '
        'Password=*****;'
        )

cursor = cnx.cursor()
sql = "set schema dustin"
cursor.execute(sql)
cursor.commit()

sql = "CREATE TABLE dustin.tmp(col1 INT, col2 INT, PRIMARY KEY(col1))"
cursor.execute(sql)
cursor.commit()

sql = "INSERT INTO dustin.tmp (col1, col2) VALUES ( 1, 2)"
cursor.execute(sql)
cursor.commit()

sql = "INSERT INTO dustin.tmp (col1, col2) VALUES ( 9, 2)"
cursor.execute(sql)
cursor.commit()
```

#### Read the table we created 
cat read_db.py -> 
```import pyodbc
import pandas

cnx = pyodbc.connect(
        'Driver=IBM i Access ODBC Driver; '
        'System=*****; '
        'UserID=*****; '
        'Password=*****;'
        )

sql = "Select * from dustin.tmp"
data = pandas.read_sql(sql, cnx)
print(data)
```

And the output as expected ->
python read_db.py
```
   COL1  COL2
0     1     2
1     9     2
```




