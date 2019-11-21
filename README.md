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




cat /etc/odbcinst.ini





