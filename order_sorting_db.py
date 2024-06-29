import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()

sql = "SELECT * from mahasiswa ORDER BY nama DESC" #sort secara descending

myCursor.execute(sql)

hasil = myCursor.fetchall()

for i in hasil:
    for j in i:
        print(j , end=" ")
    print("")

