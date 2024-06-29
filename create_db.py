import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

db = mydb.cursor()

# cara membuat data base
db.execute("CREATE DATABASE IF NOT EXISTS contoh")

# cara melihat data base
# db.execute("SHOW DATABASES")
# for i in db:
#     print (i)

