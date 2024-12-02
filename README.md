# jeu-pendu-
Introduction : L'application "Jeu du Pendu" est un jeu classique de devinette de mots, implémenté avec une interface graphique utilisant la bibliothèque Tkinter pour Python. Dans ce jeu, le joueur doit deviner un mot en proposant des lettres, tout en ayant un nombre limité de tentatives. Chaque mauvaise tentative rapproche le joueur de la "perte", tandis que chaque bonne tentative rapproche du mot complet.

Fonctionnalités principales :

Sélection aléatoire du mot :

Le jeu choisit un mot aléatoire parmi une liste pré-définie (par exemple, "python", "pendu", "informatique", etc.).
Interface graphique :

L'interface est créée avec Tkinter, offrant une expérience utilisateur agréable.
Un champ de saisie permet au joueur de proposer une lettre à chaque tour.
Le jeu affiche le mot à deviner sous forme de lettres et d'espaces (_), et met à jour l'affichage après chaque tentative.
Un compteur d'essais restants est affiché pour indiquer combien de tentatives le joueur peut encore faire avant de perdre.
Une zone d'affichage est présente pour montrer une image du "pendu", qui change selon les tentatives restantes. Si les tentatives arrivent à zéro, l'image du pendu apparaît, signalant la perte du joueur.
Messages de victoire et de défaite :

Si le joueur devine correctement toutes les lettres du mot, une animation de texte s'affiche avec le message "Félicitations ! Vous avez deviné le mot !" et le jeu se termine.
Si le joueur perd en épuisant toutes ses tentatives sans avoir trouvé le mot, un message "Dommage, vous avez perdu !" apparaît dans l'interface.
Recommencer la partie :

Après une victoire ou une défaite, le joueur peut cliquer sur un bouton "Recommencer" pour réinitialiser le jeu et démarrer une nouvelle partie. Le mot à deviner et l'état du jeu sont réinitialisés.
Gestion des lettres proposées :

Le jeu garde une trace des lettres déjà proposées par le joueur, afin d'éviter les répétitions.
Si une lettre a déjà été proposée, le joueur est informé de cette répétition.
Design et esthétique :

La couleur de fond de l'application est claire et agréable, avec un contraste entre les éléments interactifs et l'arrière-plan.
Les messages de victoire et de défaite sont colorés de manière appropriée (vert pour la victoire, rouge pour la défaite) pour une meilleure lisibilité et pour renforcer l'impact émotionnel du jeu.
L'image du pendu est intégrée dans l'interface et change en fonction du nombre de tentatives restantes. Cela ajoute une dimension visuelle au jeu, rendant l'expérience plus immersive.
Technologies utilisées :

Python : Langage de programmation principal.
Tkinter : Bibliothèque pour créer l'interface graphique.
Pillow (PIL) : Pour le traitement et l'affichage des images du pendu.
Public cible :

Cette application est destinée à tous les amateurs de jeux de réflexion, des enfants aux adultes. Elle peut être utilisée pour pratiquer l'orthographe et le vocabulaire tout en s'amusant.
Conclusion : Le "Jeu du Pendu" est une version simple mais interactive du jeu classique, avec une interface graphique claire et moderne. Il propose une expérience de jeu agréable avec des éléments visuels et un retour immédiat sur les actions du joueur.
