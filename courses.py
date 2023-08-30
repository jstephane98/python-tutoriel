print('-' * 5 + ' Gestion des courses ' + '-' * 5)

choice = ""
liste_course = []

while choice != "5":
    choice = input("""Choisissez une actions: 
                   1. Ajouter un élément.
                   2. Retirer un élément.
                   3. Afficher la liste des courses.
                   4. Vider la liste.
                   5. Quitter.
                   """)
    if choice == "1":
        element = input("Entrer un élément: ")
        liste_course.append(element.lower())
    elif choice == "2":
        element = input("Entrer l'élément que vous voulez retirer: ")
        if element.lower() in liste_course :
            liste_course.remove(element.lower())
    elif choice == "3":
        for i, element in enumerate(liste_course, 1):
            print(f"{i}. {element}")
    elif choice == "4":
        liste_course.clear()
    elif choice == "5" :
        print("Vous êtes sorti !!")
        break
    else:
        print("Choix non disponible !!!")
    print('*' * 25)