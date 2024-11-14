## Utilisez-les!


Ajoute un livre dans la bd.
````
{
    "titre": "Les Aventures de L'espace",
    "auteur": "Jeanne Dupont",
    "annee": 2021,
    "nb_pages": 350,
    "nb_chapitres": 20
}
````
````
{
    "titre": "Mystères du Temps",
    "auteur": "Alexandre Martin",
    "annee": 2018,
    "nb_pages": 220,
    "nb_chapitres": 12
}
````


### Levera une erreur
````
{
    "titre": "Les Aventures de L'espace",
    "auteur": "Jeanne Dupont",
    "nb_pages": 350,
    "nb_chapitres": 20
}
````

````
{
  "error": "Error validating against schema",
  "errors": [
    "'annee' is a required property"
  ]
}
````