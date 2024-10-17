CREATE TABLE utilisateur (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    courriel TEXT,
    date_inscription date,
    mot_de_passe_hash TEXT NON NULL,
    mot_de_passe_salt TEXT NON NULL
)