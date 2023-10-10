import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# Créer une table
c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
)
""")

# Insérer des données dans une table
parameters = {
    "prenom": "PAUL",
    "nom": "DUPOND"
}

c.execute("INSERT INTO employees VALUES (:prenom, :nom)", parameters)

# Récupérer toutes les données d'une table
parameters = {
    "prenom": "PAUL"
}

c.execute("SELECT * FROM employees")

donnees = c.fetchall()

print(donnees)

# Récupérer le premiér élement d'une table

c.execute("SELECT * FROM employees")

premier = c.fetchone()
print(premier)

# Faire une recherche

c.execute("SELECT * FROM employees WHERE prenom=:prenom", parameters)

search = c.fetchone()
print(search)

# Mise à jour
parameters = {
    "nom": "JACK",
    "prenom": "PAUL"
}
c.execute("UPDATE employees SET nom=:nom WHERE prenom=:prenom", parameters)

# Suppression des données
c.execute("DELETE FROM employees WHERE prenom=:prenom", parameters)

conn.commit()

conn.close()
