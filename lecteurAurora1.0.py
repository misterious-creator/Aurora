#Copyright (c) 2026 Misteriouscreator

from PIL import Image
from tkinter import filedialog
import os
fichier = filedialog.askopenfilename(
    title="Sélectionnez un fichier Aurora",
    filetypes=[("Fichier Aurora", "*.png")]
)
o = []
nom_fichier = os.path.basename(fichier)
a = nom_fichier.split(" ")
pr = int(a[2].replace(".png","").replace("pr",""))
r = int(a[1].replace("r",""))
image = Image.open(fichier)
largeur,hauteur = image.size
nbpixel  = largeur*hauteur-pr
for i in range(nbpixel):
    x = i % largeur
    y = i // largeur
    couleur = image.getpixel((x, y))
    o.append(couleur[0])
    o.append(couleur[1])
    o.append(couleur[2])
if r == 0:
    octet = o
else:
    octet = o[:-r]
octets = bytes(octet)
nomfichier = a[0]
with open(nomfichier,"wb")as f:
    f.write(octets)