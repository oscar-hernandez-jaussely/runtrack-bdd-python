
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

cur = db.cursor(buffered=True)

cur.execute("CREATE DATABASE data_test;")

cur.execute("USE data_test;")

cur.execute("CREATE TABLE employes (id INTEGER PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL, id_service INTEGER);")

cur.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES ('Doe', 'John', 1500, 1), ('Hawthorne', 'James', 1750, 2), ('Maxson', 'Arthur', 5000, 6), ('Garvey', 'Preston', 2100, 5), ('Valentine', 'Nick', 1600, 3), ('Morgan', 'Henry', 4600, 4);")

cur.execute("SELECT * FROM employes WHERE salaire>3000;")
for i in cur:
    print(i)

cur.execute("CREATE TABLE services (id INTEGER PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255));")

cur.execute("INSERT INTO services (nom) VALUES ('Mission de reconnaissance'), ('Elimination de cibles'), ('Recherche et récupération'), ('Recherche et destruction'), ('Capture de troupes ennemies'), ('Pacification atomique de zone cible');")

cur.execute("SELECT * FROM employes")
for i in cur:
    print(i)

cur.execute("SELECT * FROM services")
for i in cur:
    print(i)

db.commit()

class CRUD: 

    cur.execute("USE data_test;")

    # --- CREATE --- # 

    def add_employe():
        nom = input("Nom ? ")
        prenom = input("Prénom ? ")
        salaire = input("Salaire ? ")
        id_service = input("ID service ? ")
        cur.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES ('{}', '{}', '{}', '{}');".format(nom, prenom, salaire, id_service))
        print ("Added data in table")
        db.commit()

    # ---------------- #


    
    # --- READ --- #

    def get_employes():
        cur.execute("SELECT * FROM employes")
        for i in cur:
            print(i)
        
    # ---------------- #



    # --- UPDATE --- #

    def update_employe():
        id = input("Data ID ? ")
        nom = input("Nom ? ")
        prenom = input("Prénom ? ")
        salaire = input("Salaire ? ")
        id_service = input("ID service ? ")
        cur.execute("UPDATE employes SET nom='{}', prenom='{}', salaire={}, id_service={} WHERE id={};".format(nom, prenom, salaire, id_service, id))
        print("Data updated")
        db.commit()

    # ---------------- #



    # --- DELETE --- #

    def del_employe():
        id = input("Data ID ? ")
        cur.execute("DELETE FROM employes WHERE id={}".format(id))
        print("Data deleted")
        db.commit()
    
    # ---------------- #

