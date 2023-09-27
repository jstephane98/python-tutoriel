from pathlib import Path
import random

ext_dic = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".mp4": "Vidéos",
    ".mov": "Vidéos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".mp3": "Musiques",
    ".ttf": "Polices",
    ".exe": "Applications",
    ".msi": "Applications",
    ".torrent": "Torrents",
}

# Create Radom file 
# tri_dir = Path.home() / "Tri"
# tri_dir.mkdir(exist_ok=True)
# for directory in ext_dic:
#     for f in range(0, random.randint(1, 10)):
#         out_file = tri_dir / (str(f) + directory)
#         out_file.touch()

# Tri files
tri_dir = Path.home() / "Downloads"
tri_dir.mkdir(exist_ok=True)
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = tri_dir / ext_dic.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)