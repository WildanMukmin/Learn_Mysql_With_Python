import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()
sql = "DROP TABLE mahasiswa"
myCursor.execute(sql)
mydb.commit()