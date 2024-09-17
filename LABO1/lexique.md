### Lexique des balises HTML utilisé dans le LABO1

Ce lexique explique les balises HTML spécifiques que vous avez utilisées dans le cadre de votre premier laboratoire. Chaque balise a un rôle précis dans la construction d'une page web. Nous commencerons par une section dédiée aux balises `<meta>`, essentielles pour fournir des informations aux moteurs de recherche et améliorer l'accessibilité du site.

---

## Les balises `<meta>`

Les balises `<meta>` sont des métadonnées incluses dans la section `<head>` d'un document HTML. Elles ne sont pas visibles par les utilisateurs finaux mais sont lues par les moteurs de recherche, les navigateurs web et les robots d'indexation. Ces balises fournissent des informations importantes qui influencent la manière dont la page est indexée et affichée. Voici un aperçu des balises `<meta>` couramment utilisées, que vous avez dans votre document :

### `<meta charset="UTF-8">`
- **Description :** Définit l'encodage des caractères utilisés dans la page. UTF-8 est un encodage universel qui permet de représenter presque tous les caractères de toutes les langues. Cela assure que les caractères spéciaux, comme les accents en français, sont correctement affichés.
- **Exemple d'utilisation :**
  ```html
  <meta charset="UTF-8">
  ```
- **Importance :** Sans cet encodage, les caractères comme `é`, `à`, ou `ç` pourraient apparaître de manière incorrecte sur la page.

### `<meta name="description" content="...">`
- **Description :** Fournit une courte description du contenu de la page. Cette description est souvent affichée dans les résultats de recherche des moteurs de recherche en dessous du titre de la page. C’est un résumé concis de l’objectif ou du contenu principal de la page.
- **Exemple d'utilisation :**
  ```html
  <meta name="description" content="Voici mon CV, si vous désirez m'embaucher n'hésitez pas à visiter ce site!">
  ```
- **Importance :** Cette balise aide les moteurs de recherche à comprendre le contenu de la page et peut inciter les utilisateurs à cliquer sur le lien en lisant une description pertinente.

### `<meta name="author" content="...">`
- **Description :** Spécifie l'auteur de la page web. Cette information peut être utile pour les administrateurs du site, les moteurs de recherche et les navigateurs, mais n'est pas toujours visible par les utilisateurs.
- **Exemple d'utilisation :**
  ```html
  <meta name="author" content="Aaron Osorio">
  ```
- **Importance :** Cela permet de reconnaître l’auteur du document, ce qui peut être utile pour la gestion et la crédibilité du contenu.

### `<meta name="keywords" content="...">`
- **Description :** Liste de mots-clés associés au contenu de la page. Bien que moins utilisée aujourd'hui par certains moteurs de recherche comme Google, cette balise aide toujours à fournir un contexte supplémentaire sur les termes associés au contenu.
- **Exemple d'utilisation :**
  ```html
  <meta name="keywords" content="CV, emploi, recherche d'emploi, job, job pour Aaron">
  ```
- **Importance :** Autrefois cruciale pour le référencement (SEO), elle permet aux moteurs de recherche de comprendre rapidement les thèmes abordés sur la page. Elle reste pertinente dans certains systèmes de gestion de contenu.

### `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- **Description :** Contrôle la manière dont la page est affichée sur des appareils mobiles. Le paramètre `width=device-width` signifie que la largeur de la page doit correspondre à celle de l'appareil. Le paramètre `initial-scale=1.0` indique que la page doit être affichée avec un zoom initial de 100%.
- **Exemple d'utilisation :**
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```
- **Importance :** Crucial pour la conception de sites web adaptatifs (responsive design), cette balise garantit que la page est correctement mise à l'échelle sur les écrans de différentes tailles, en particulier les smartphones et tablettes.

### `<meta name="robots" content="index, follow">`
- **Description :** Donne des instructions aux moteurs de recherche sur la manière de traiter la page. L'attribut `index` signifie que la page doit être indexée, tandis que `follow` indique que les liens sur la page doivent être suivis.
- **Exemple d'utilisation :**
  ```html
  <meta name="robots" content="index, follow">
  ```
- **Importance :** Cette balise est essentielle pour le référencement naturel (SEO). Elle indique aux moteurs de recherche s'ils doivent ou non indexer la page et suivre les liens vers d'autres pages.

---

## Autres balises utilisées dans le document

Voici un récapitulatif rapide des autres balises présentes dans le document :

### `<html lang="fr">`
- **Description :** La balise `<html>` englobe tout le contenu de la page. L'attribut `lang="fr"` précise que la langue principale de la page est le français, ce qui améliore l'accessibilité et aide les moteurs de recherche à mieux comprendre le contenu.

### `<head>`
- **Description :** Contient des métadonnées et des éléments tels que le titre de la page, les balises `<meta>`, les feuilles de style, et les scripts. Cette section est invisible pour les utilisateurs.

### `<title>`
- **Description :** Définit le titre qui apparaît dans l'onglet du navigateur. Ce titre est également utilisé par les moteurs de recherche comme titre principal dans les résultats.

### `<body>`
- **Description :** Contient le contenu visible de la page, comme les textes, images, liens, et autres éléments interactifs.

### `<header>`
- **Description :** Représente une section d'en-tête souvent utilisée pour afficher le titre ou un logo.

### `<h1>`, `<h2>`, `<h3>`
- **Description :** Ces balises structurent les titres de la page. `<h1>` est le titre principal, tandis que `<h2>` et `<h3>` sont des sous-titres de différents niveaux.

### `<ul>`, `<li>`
- **Description :** Ces balises créent des listes à puces (`ul` pour "unordered list") et chaque élément de la liste est contenu dans une balise `<li>` (list item).

### `<table>`, `<tr>`, `<th>`, `<td>`
- **Description :** Ces balises sont utilisées pour créer un tableau. `<table>` représente l'ensemble du tableau, `<tr>` représente une ligne, `<th>` définit les en-têtes de colonne, et `<td>` représente une cellule de données.

### `<a>`
- **Description :** Crée des liens hypertextes vers des adresses externes ou internes. L'attribut `href` spécifie la destination du lien, et `mailto:` permet d'envoyer un e-mail à une adresse spécifiée.

### `<footer>`
- **Description :** Section du pied de page, généralement utilisée pour inclure des informations légales ou de contact, comme le copyright.