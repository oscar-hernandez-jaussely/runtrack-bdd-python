
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "laplateforme"
)

cur = db.cursor()

cur.execute("SELECT * FROM etudiants")

res = cur.fetchall()

for line in res:
    print (line)

