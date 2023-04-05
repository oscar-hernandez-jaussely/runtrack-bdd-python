
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "laplateforme"
)

cur = db.cursor()

cur.execute("SELECT nom, capacite FROM salles")

res = cur.fetchall()

print(res)

