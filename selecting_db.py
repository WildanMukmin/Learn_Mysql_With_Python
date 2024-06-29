import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()

myCursor.execute("select npm from mahasiswa where id=3")

# hasil = myCursor.fetchall()

# # for i in hasil:
# #     print(i[1])

hasil = myCursor.fetchone()

for i in hasil:
    print(i)