
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "laplateforme"
)

cur = db.cursor()

cur.execute("SELECT SUM(superficie) FROM etage")

output = []

for row in cur:
    output.append(int(row[0]))

res = output[0]

print("La superficie de La Plateforme est de {} m2".format(res))

