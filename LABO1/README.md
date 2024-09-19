LABO 1 - Partie 1 : HTML de base
============

Vous devez construire une page web contenant votre CV. Vous ne
devez utiliser que le HTML, sans CSS. Évidemment, votre page web ne sera pas la
plus jolie en n'utilisant que les valeurs par défaut du fureteur.

Utilisez Google Chrome pour tester l'affichage de votre page.

Objectifs
---------

* Manipuler les éléments de base du HTML.
* Valider un document HTML.

Exercices
---------

Après chaque exercice, assurez-vous de valider votre document HTML à l'aide du
[Validateur du W3C](https://validator.w3.org/) et de corriger toutes les erreurs
et tous les avertissements.

1. Construisez un document HTML qui servira à contenir votre CV. Au début, le
   `body` ne doit contenir que votre nom. Utilisez la balise `h1` pour votre
   nom.

2. Sous votre nom, inscrivez vos coordonnées de correspondance (adresse, numéro
   de téléphone, courriel). Affichez l'adresse comme sur une enveloppe postale
   et le téléphone et le courriel chacun sur sa propre ligne. Utilisez les
   balises `p` et `br` pour y parvenir. Il ne doit pas y avoir de séparation de
   paragraphe entre les lignes des coordonnées de correspondance.

3. Ajoutez une section décrivant vos objectifs de carrière. Dans toutes les
   sections, il doit d'abord y avoir un titre (balise `h2`) et ensuite le
   contenu. Dans ce cas-ci, le contenu doit être un paragraphe expliquant vos
   objectifs professionnels. Placez une ligne horizontale (balise `hr`) entre
   chaque section.

4. Transformez le courriel dans vos coordonnées de correspondance en lien.
   Utilisez la balise `a` avec un `mailto`.

5. Ajoutez une section sur les technologies que vous maîtrisez. La section doit
   contenir une liste non ordonnée (balises `ul` et `li`) de langages de
   programmation et d'outils informatiques que vous connaissez.

6. Ajoutez une section sur vos expériences professionnelles. La section doit
   contenir un tableau (balises `table`, `thead`, `tbody`, `tr`, `th`,
   `td`). Le tableau doit contenir une rangée d'entêtes et une rangée pour
   chaque emploi que vous avez eu. Placez au moins 3 emplois. Le tableau doit
   contenir 4 colonnes : l'année de l'emploi, le titre de votre poste, le nom de
   l'entreprise, une liste ordonnée (balises `ol` et `li`) de vos
   responsabilités triées par ordre d'importance.

7. Ajoutez une photo de vous à votre CV (balise `img`), positionnée
   immédiatement au-dessus de votre nom, au début du document.

LABO 1 - Partie 2 : CSS
===

Le CSS joue un grand rôle dans la conception d'un site web : il gère toute la
présentation visuelle du site. Sans le CSS, les sites web seraient bien
ennuyants à regarder.

Au début de la séance, les moniteurs feront une courte présentation de
l'inspecteur d'éléments de Google Chrome. Il s'agit d'un outil très utile pour
vérifier quels styles CSS s'appliquent sur un élément en particulier. Il est
possible d'activer et de désactiver des styles pour expérimenter et déboguer.

Objectifs
---------

* Manipuler le CSS.
* Manipuler l'inspecteur d'éléments de Chrome.

Exercices
---------

1. Créez un site web contenant un titre (`h1`) et 3 paragraphes. Utilisez du
   Lorem Ipsum pour le texte des paragraphes. Ajoutez une feuille de style CSS à
   notre document HTML grâce à la balise `link`.

2. Ajoutez un style sur l'élément `h1` pour que le titre soit rouge et souligné.

3. Faites en sorte que le titre soit plus petit de 25%.

4. Ajoutez des classes différentes pour chacun des paragraphes de la page. À
   l'aide de ces classes, faites en sorte que le premier paragraphe soit bleu,
   le deuxième blanc et le troisième rouge.

5. Placez votre nom dans un élément `span` en plein milieu du premier
   paragraphe.

6. Ajoutez un `id` sur l'élément contenant votre nom et utilisez cet `id` pour
   faire en sorte que votre nom soit affiché en gras. Grâce au sélecteur
   `:hover`, faites en sorte que le curseur de la souris devienne une main
   (comme si c'était un lien cliquable) dès que la souris passe au-dessus de
   votre nom.

7. Changez la police de caractères pour tous les paragraphes, mais pas le titre.

8. Ajoutez une marge significative au deuxième paragraphe.

9. Placez un formulaire avec 3 champs texte et 3 labels dans le bas de la page. Tentez
   d'aligner les 3 champs texte sans utiliser de tableau. Regardez les éléments
   HTML `input` (avec l'attribut `type="text"`) et `label`.