from pathlib import Path
p = Path.home() / "Downloads"

# Créer un fichier
# p.mkdir(exist_ok=True, parents=True)

# Crée un fichier
# p.touch()

# supprimer un fichier
# p.unlink()

# Supprimer un dossier vide
# p.rmdir()

# extenxion d'un fichier
# p.suffix (.'...')

# Supprimer un dossier de manière récursive avec ces enfants
# import shutil
# shutil.rmtree(p)

# Récupérer tous les dossiers et fichiers à l'intérieur d'un dossier
# for file in p.iterdir():
#     print(file.name)
# [print(f) for f in p.iterdir() if f.is_file()]

# Rechercher un type de fichier dans un dossier
# [print(f.name) for f in p.glob('*.rar')]
#  Rechercher un type de fichier de manière récusirve dans un dossier
# [print(f.name) for f in p.rglob('*.ttf')]