import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()

myCursor.execute(""" CREATE TABLE mahasiswa(
    id int primary key auto_increment, 
    nama VARCHAR(100),
    npm CHAR(10),
    kelas char(1),
    jusuran varchar(100)
)
                 """)