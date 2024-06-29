import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()

sqlCommand = "UPDATE mahasiswa SET nama='inilahh akhirnya' WHERE id=5"

myCursor.execute(sqlCommand)

mydb.commit()


