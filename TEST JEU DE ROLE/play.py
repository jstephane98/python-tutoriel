from random import randint

player = {
    "health": 50,
    "attack": [5, 10],
    "potions": {
        "count": 3,
        "health_restore": [10, 35]
    },
}

ennemi = {
    "health": 50,
    "attack": [5, 15]
}

STEP_PASS = False;

while player['health'] > 0 and ennemi['health'] > 0:
    # Player Attack
    if not STEP_PASS:
        choice = input("Souhaitez vous attaquer (1) ⚔️  ou utiliser une potion (2) 🍯 ? ")

        if not choice.isdigit() or choice not in ["1", "2"]:
            print("-" * 25)
            print("Veillez entrer un nombre entier: (1) ou (2)")
            continue

        if choice == "1":
            attackPlayer = randint(player["attack"][0], player["attack"][1])
            ennemi['health'] -= attackPlayer
            print(f"⚔️: Votre ennemi a subit {attackPlayer} dégats de votre part.")
        else:
            if player["potions"]['count'] > 0:
                soint = randint(player["potions"]['health_restore'][0], player["potions"]['health_restore'][1])
                player["health"] += soint
                player["potions"]['count'] -= 1
                print(f"❤️: Vous avez restauré votre santé de {soint} point de vie, il vous reste {player['potions']['count']} potions")
                STEP_PASS = True
            else:
                print("Vous n'avez plus de potion.")
                print("-" * 25)
                continue
    else:
        print("Vous passez votre tour...")
        STEP_PASS = False

    if ennemi["health"] <= 0:
        print("-" * 25)
        break

    # Annemi Attack
    attackEnnemi = randint(ennemi["attack"][0], ennemi["attack"][1])
    player['health'] -= attackEnnemi

    print(f"⚔️: Vous avez subit {attackEnnemi} dégats de l'ennemi.")
    print(f"Il vous reste {player['health'] if player['health'] >= 0 else 0} ❤️  de point de vie.")
    print(f"Il en reste {ennemi['health']} ❤️  chez votre ennemi.")
    print("-" * 25)

if ennemi["health"] <= 0 :
    print("Vous avez gagner la partie 🥇")
else:
    print("Vous avez perdu 💔")
