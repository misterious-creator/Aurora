# Aurora

Aurora est un projet de **format de stockage expérimental** qui permet de représenter les données d'un fichier sous forme d'une image.

Le projet est actuellement en **version 1.0**.

## Concept

Aurora transforme les données binaires d'un fichier en pixels RGB.

Chaque groupe de **3 octets** devient un pixel :

```text
Octet 1 → Rouge (R)
Octet 2 → Vert  (G)
Octet 3 → Bleu  (B)
```

L'image peut ensuite être décodée afin de récupérer les données originales.

---

## Conservation des données

Aurora conserve la taille exacte du fichier original grâce à une information **`r`** dans le nom du fichier.

Exemples :

```text
fichier.txt r0 pr1.png
fichier.txt r1 pr0.png
fichier.txt r2 pr3.png
```

### `r`

**`r`** indique le nombre d'octets ajoutés artificiellement au dernier pixel.

* **`r0`** → aucun octet ajouté
* **`r1`** → 1 octet ajouté
* **`r2`** → 2 octets ajoutés

Les octets de remplissage utilisent actuellement la valeur **`32`** (**`0x20`**), qui correspond à un espace.

### `pr`

**`pr`** indique le nombre de pixels supplémentaires ajoutés pour compléter la dernière ligne de l'image.

Les pixels de remplissage sont :

```text
(32, 32, 32)
```

**`r`** et **`pr`** ont donc deux fonctions différentes.

---

## Organisation de l'image

Aurora calcule automatiquement une taille d'image proche d'un carré.

```text
largeur = ceil(sqrt(nombre_de_pixels))
hauteur = ceil(nombre_de_pixels / largeur)
```

Les pixels supplémentaires nécessaires pour remplir l'image sont ensuite ajoutés.

---

## Exemple

Un fichier contenant :

```text
Hello
```

contient les octets :

```text
48 65 6C 6C 6F
```

Aurora les regroupe ainsi :

```text
48 65 6C
6C 6F 20
```

Ce qui produit deux pixels :

```text
(R=72, G=101, B=108)
(R=108, G=111, B=32)
```

Le fichier peut ensuite être reconstruit à partir de ces pixels.

---

# Fonctionnement

Aurora utilise deux opérations principales :

### Encodage

```text
Fichier
   ↓
Données binaires
   ↓
Groupes de 3 octets
   ↓
Pixels RGB
   ↓
Image Aurora
```

### Décodage

```text
Image Aurora
   ↓
Pixels RGB
   ↓
Octets
   ↓
Données binaires originales
   ↓
Fichier
```

Le système `r` permet de supprimer les octets de remplissage ajoutés au dernier pixel.

Le système `pr` permet de déterminer quels pixels ont été ajoutés uniquement pour compléter les dimensions de l'image.

---

# État du projet

Aurora est actuellement en développement.

### Fonctionnel

* [x] Encodage binaire → pixels RGB
* [x] Décodage pixels RGB → données binaires
* [x] Conservation de la taille originale avec **`r`**
* [x] Remplissage de l'image avec **`pr`**
* [x] Génération automatique de la taille de l'image
* [x] Gestion des octets de remplissage
* [x] Reconstruction des données originales

### En développement

* [ ] Améliorer la gestion des erreurs
* [ ] Ajouter un système de compression
* [ ] Ajouter un système de chiffrement (prévu le 31 octobre 2026)
* [ ] Définir davantage le format Aurora
* [ ] Améliorer les performances pour les gros fichiers
* [ ] Optimiser le stockage des données
* [ ] Améliorer la compatibilité avec différents formats de fichiers
* [ ] Ajouter des métadonnées au format Aurora
* [ ] Développer une spécification complète du format

---

# Format Aurora

Le format Aurora est basé sur la représentation directe des données binaires sous forme de pixels RGB.

Chaque pixel contient exactement **3 octets de données** :

```text
Pixel = R + G + B
```

Par exemple :

```text
Données :
48 65 6C 6C 6F

Pixels :
48 65 6C
6C 6F 20
```

Les informations supplémentaires nécessaires au décodage sont actuellement représentées dans le nom du fichier avec :

```text
r
pr
```

Le format pourra évoluer dans les prochaines versions afin de rendre ces informations plus robustes et indépendantes du nom du fichier.

---

# Objectifs futurs

Les principaux objectifs du projet sont :

* créer une spécification complète du format Aurora ;
* permettre le stockage de données arbitraires dans une image ;
* améliorer la fiabilité du décodage ;
* réduire la taille des fichiers grâce à la compression ;
* permettre le chiffrement des données ;
* améliorer les performances sur les gros fichiers ;
* rendre le format facilement implémentable dans différents langages ;
* assurer une compatibilité entre différentes versions du format.

---

# Technologies utilisées

Actuellement :

* **Python**
* **Pillow (PIL)**

D'autres technologies ou bibliothèques pourront être ajoutées si elles sont nécessaires à l'évolution du format.

---

# Important

Aurora est actuellement un **format expérimental**.

Il ne faut pas considérer Aurora comme un système de stockage ou de chiffrement sécurisé.

Les futurs systèmes de compression et de chiffrement sont encore en développement.

La compatibilité entre les différentes versions du format peut également évoluer.

---

# Licence

Le projet est actuellement en développement.

Les informations concernant la licence seront ajoutées prochainement.

---

# À propos

Aurora est un projet expérimental visant à explorer une idée simple :

> **Et si un fichier pouvait être représenté directement par une image ?**

Le but est d'explorer les possibilités de cette représentation, de construire un format cohérent autour de celle-ci et de développer progressivement un véritable format de stockage.

Aurora cherche notamment à établir une méthode permettant de convertir des données binaires en données visuelles tout en conservant la possibilité de reconstruire exactement les données originales.

Le projet pourra progressivement évoluer vers un format plus complet intégrant notamment la compression, le chiffrement, les métadonnées et différentes optimisations.

Si le projet vous intéresse, n'hésitez pas à ouvrir une **Issue** ou à proposer une contribution.
# Je cherche de l'aide pour créer une interface

Aurora fonctionne actuellement sans interface graphique.

Je cherche des personnes intéressées pour m'aider à **concevoir et développer une interface graphique pour Aurora**.

Le projet est personnel et je cherche principalement des personnes souhaitant **contribuer gratuitement à un projet open source**, apprendre, expérimenter ou participer au développement.

### Compétences utiles

Vous pouvez aider même si vous ne maîtrisez pas toutes ces technologies.

Les compétences particulièrement utiles seraient :

* Python
* Tkinter
* PySide / PyQt
* UI/UX
* Design d'interfaces
* Git / GitHub

Je suis également ouvert aux propositions concernant la technologie à utiliser pour créer l'interface.

### Comment contribuer

Vous pouvez :

1. Ouvrir une **Issue** pour proposer une idée.
2. Proposer un concept d'interface.
3. Créer une branche et proposer une **Pull Request**.
4. Participer directement au développement de l'interface.
5. Proposer une autre technologie adaptée au projet.

Même une petite contribution est la bienvenue.
