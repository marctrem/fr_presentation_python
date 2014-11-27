# De Java vers Python

Le but de cette présentation est de permettre aux gens connaissant Java d'être à l'aise en Python le plus rapidement possible.

## Sujets couverts

### Volet comparaison

- Indentation
- Assignation de variable
- Chaînes de caractères
- Listes, dictionnaires
- Conversions de type
- Taille d'un int (Promotion numérique)
- Control de flot
- stdin
- Fichiers
- Fonctions
- Pourquoi Python est 'lent'
- Classes
- Opérateurs de comparaison

### Volet spécificitées

- Évaluation et exécution
- Lambdas
- Générateurs
- Décorateurs
- Compréhension de liste
- Compréhension de dictionnaire

### Théorie

- Map
- Reduce (foldl)
- Foldr
- Filter

### Exemples

- Mini Traducteur
- Word Count (collections.defaultdict)

### Exercices

#### Project Euler
- https://projecteuler.net/problem=1 (Multiples of 3 and 5)
- https://projecteuler.net/problem=2 (Even Fibonacci numbers)
- https://projecteuler.net/problem=13 (Large sum)
- https://projecteuler.net/problem=14 (Longest Collatz sequence)
- https://projecteuler.net/problem=16 (Power digit sum)
- https://projecteuler.net/problem=92 (Square digit chains)


Ajoutez-moi! 375454_ce5d7f96d544f136341387a686097269
#### Fait maison
- Générateur: Itérateur dans un arbre binaire
- Décorateur: Dis moi qui tu es. (Injection dans les globales)
- Décorateur: Tu dois être dans le bon groupe. (Injection et filtre avec globales)
- Word count à la Harry Potter!
### Matériel requis

- Python 3

### Construire le distribuable

Avoir Node, Grunt, Bower, Ruby et Compass. (assez stardard comme stack)


-`cd presentation`

-`npm install grunt-cli -g` Installer Grunt
-`npm install bower -g`Installer Bower

-`npm install` Installer les paquets Node locaux requis
-`bower install` Installer les libraries web

-`bower` pour partir le serveur en live reload
-`bower dist` pour créer le dossier distribuable.

