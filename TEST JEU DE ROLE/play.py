from random import randint

player = {
    "health": 50,
    "attack": [5, 10],
    "potions": {
        "count": 3,
        "health_restore": [5, 25]
    },
}

ennemi = {
    "health": 50,
    "attack": [5, 15]
}

while player['health'] > 0 and ennemi['health'] > 0:
    choice = input("Souhaitez vous attaquer (1) ⚔️  ou utiliser une potion (2) 🍯 ? ")

    if not choice.isdigit():
        print("-" * 25)
        print("Veillez entrer un nombre entier: (1) ou (2)")
        continue

    choice = int(choice)
    if choice not in [1, 2] :
        print("-" * 25)
        print("Veillez entrer un nombre valide: (1) ou (2)")
        continue

    if choice == 1:
        # Player Attack
        attackPlayer = randint(player["attack"][0], player["attack"][1])
        ennemi['health'] -= attackPlayer
        print(f"⚔️: Votre ennemi a subit {attackPlayer} dégats de votre part.")
    else:
        if player["potions"]['count'] > 0:
            soint = randint(player["potions"]['health_restore'][0], player["potions"]['health_restore'][1])
            player["health"] += soint
            player["potions"]['count'] -= 1
            print(f"❤️: Vous avez restauré votre santé de {soint} point de vie")
            print("Vous passez votre tour...")
        else:
            print("Vous n'avez plus de potion.")
            print("-" * 25)
            continue

    if ennemi["health"] < 0:
        print("-" * 25)
        break

    # Annemi Attack
    attackEnnemi = randint(ennemi["attack"][0], ennemi["attack"][1])
    player['health'] -= attackEnnemi

    print(f"⚔️: Vous avez subit {attackEnnemi} dégats de l'ennemi.")
    print(f"Il vous reste {player['health']} ❤️  de point de vie, il en reste {ennemi['health']} ❤️  chez votre ennemi.")
    print("-" * 25)

if ennemi["health"] < 0 :
    print("Vous avez gagner la partie 🥇")
else:
    print("Vous avez perdu 💔")
