#Copyright (c) 2026 Misteriouscreator

import tkinter as tk
import os
import math
from PIL import Image
from tkinter import filedialog
fichier = filedialog.askopenfilename(
    title="Sélectionnez un fichier",
    filetypes=[
        ("Tous les fichiers", "*.*"),
        ("Fichiers texte", "*.txt"),
        ("fichier compressé", ("*.zip", "*.7z", "*.tar"))
    ]
)
nom_fichier = os.path.basename(fichier)
pixel = []
with open(fichier, "rb") as f:
    octet = f.read()
for i in range(0, len(octet), 3):
    r = octet[i]
    if i + 1 < len(octet):
        g = octet[i + 1]
    else:
        g = 32
    if i + 2 < len(octet):
        b = octet[i + 2]
    else:
        b = 32
    pixel.append((r, g, b))
nbpixel = len(pixel)
largeur = math.ceil(math.sqrt(nbpixel))
hauteur = math.ceil(nbpixel / largeur)
pr = largeur * hauteur - nbpixel
for i in range(pr):
    pixel.append((32,32,32))
image = Image.new("RGB", (largeur, hauteur))
x = 0
y = 0
for couleur in pixel:
    image.putpixel((x,y) , couleur)
    if x == largeur - 1:
        x = 0
        y += 1
    else:
        x += 1
reste = len(octet) % 3
if reste == 0:
    r = 0
else:
    r = 3 - reste
nom = nom_fichier + " r" + str(r) + " pr" + str(pr) + ".png"
image.save(nom)