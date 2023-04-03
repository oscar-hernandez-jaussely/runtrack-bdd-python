
INSERT INTO etudiants (nom, prenom, age, email) VALUES ("Dupuis", "Martin", 18, "martin.dupuis@laplateforme.io");

SELECT e1.* FROM etudiants e1, etudiants e2 WHERE e1.nom = e2.nom AND e1.id != e2.id;

