# Règle du jeu

Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.

- Le jeu comporte **2 joueurs** : vous et un ennemi
- Vous commencez tous les 2 avec **50 points de vies**
- Votre personnage dispose de **3 potions** qui vous permettent de récupérer des points de vie
- L'ennemi de dispose d'aucune potion
- Chaque potion vous permet de récupérer un nombre aléatoire de point de vie, compris entre **15 et 50**
- Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre **5 et 10** points de vie.
- L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre **5 et 15** points de vie
- Lorsque vous utilisez une potion, **vous passer le prochain tour**.

Déroulé de la partie
Lorsque vous lancer le script, vous devez demander à l'utilisateur s'il souhaite attaquer ou utiliser une potion: ""**Souhaitez vous attaquer (1) ou utiliser une potion (2) ?**"

Cette phrase sera demander à l'utilisateur au debut de chaque tour

- Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi
- Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme 
- Si l'utilisateur choisi la 2e option (2), vous prenez une potion (vous récupérer des points de vie entre 15 et 50) et vous passez votre tour et l'ennemi pourra vous attaquez.