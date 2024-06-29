import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()

myCursor.execute("select * from mahasiswa where nama like '%da%'")

hasil = myCursor.fetchall()

for i in hasil:
    for j in i:
        print(j , end=" ")
    print("")

