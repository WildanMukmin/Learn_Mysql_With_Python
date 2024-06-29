import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "contoh"
)

myCursor = mydb.cursor()
sqlFormula = "insert into mahasiswa (nama, npm, kelas, jusuran) value(%s,%s,%s,%s)"

# mhs1 = ("Bang Will", "2317051000", "D", "Ilmu Komputer")
# myCursor.execute(sqlFormula,mhs1)

# atau mau banyak
mhs = [
    ("Wildan Mukmin", "2317051080", "D", "Ilmu Komputer"),
    ("mub", "2317051000", "D", "Ilmu Komputer"),
    ("Riskur", "2317051080", "D", "Ilmu Komputer"),
    ("Dea", "2317051080", "D", "Ilmu Komputer"),
    ("Alia", "2317051080", "D", "Ilmu Komputer")
    ]
myCursor.executemany(sqlFormula,mhs)


mydb.commit()