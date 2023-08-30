import random

print('-' * 5 + 'Nombre mystère: vous avez 5 chances' + '-' * 5)

mystery_number = random.randint(1, 15)
choice_number = 0

while choice_number < 5:
    choice = int(input("Entrer un nombre: "))
    if choice == mystery_number:
        print(f"Vous avez trouvé le nombre mystère : {mystery_number}")
        break
    choice_number += 1
    print("-" * 25)
    print('Choix non valide')
    if not choice_number < 5:
        print(f"Vous avez eu 5 chances :  et le nombre mystère est : {mystery_number}")