
CREATE TABLE etage (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    numero INTEGER,
    superficie INTEGER
);

CREATE TABLE salles (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    id_etage INTEGER,
    capacite INTEGER
);


