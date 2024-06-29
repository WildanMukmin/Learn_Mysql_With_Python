import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()
sql = "DELETE FROM mahasiswa WHERE id=7"
myCursor.execute(sql)
mydb.commit()