
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "laplateforme"
)

cur = db.cursor()

cur.execute("SELECT SUM(capacite) FROM salles")

output = []

for row in cur:
    output.append(int(row[0]))

res = output[0]

print("La capacité de toutes les salles est de : {}".format(res))

