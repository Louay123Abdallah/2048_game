# 2048_game
This is my simple open source version of 2048_game using PyQt5 modules 
# Guide du Jeu 2048

Bienvenue dans le monde de 2048 !  
Ce guide vous explique comment jouer et marquer le plus de points possible.  
Pas besoin d’être expert. Tout est simple.

---

## 1. Le Terrain de Jeu et le Début de la Partie

- Grille de **6 lignes** et **5 colonnes**
- Remplie de nombres **aléatoires**, tous des **multiples de 2** (2, 4, 8, 16, 32, 64)
- Score de départ : **0**
- Un nouveau nombre apparaît en haut, à placer dans la grille

---

## 2. Comment Jouer un Tour

1. **Choix de la colonne** : de **1 à 5**
2. **Vérification** :
   - La **case du bas** (ligne 6) de la colonne doit :
     - Être **vide (0)**, ou
     - Contenir le **même nombre**
3. **Placement** :
   - Si même nombre → **fusion** → le nombre double et s’ajoute au score
   - Si vide → le nombre est placé tel quel
4. **Réorganisation** automatique du tableau
5. **Un nouveau nombre** est généré pour le tour suivant
6. Le **score est mis à jour**
7. Vérification de **fin de partie**

---

## 3. Comment le Tableau se Réorganise (La Magie des Fusions)

### Étapes appliquées après chaque coup :

1. **Les zéros remontent (verticalement)**
   - Ex : `[4, 0, 8]` devient `[0, 4, 8]`
2. **Fusions verticales**
   - Ex : `[4, 4, 8]` devient `[0, 8, 8]` → score +8
3. **Les zéros se déplacent (horizontalement)**
   - Ex : `[4, 0, 8]` devient `[0, 4, 8]`
4. **Fusions horizontales**
   - Ex : `[4, 4, 8]` devient `[0, 8, 8]` → score +8
5. **Remontée verticale des zéros (encore)**
6. **Déplacement horizontal des zéros (encore)**

**L’ordre est crucial** pour que les fusions fonctionnent correctement.

---

## 4. Comment le Score est Calculé

- Chaque **fusion** donne des points
- Exemples :
  - `4 + 4 → 8` → score +8
  - `16 + 16 → 32` → score +32

---

## 5. Quand le Jeu se Termine (Défaite)

- Fin du jeu quand :
  - La **dernière ligne** est **pleine**
  - Aucun **placement possible** :
    - Pas de case vide
    - Pas de fusion possible
- Message : **"Fin de Jeu !"**
- Affichage du **meilleur score**

---

## 6. Comment les Nouveaux Nombres Apparaissent

- Choisis **aléatoirement**
- Au début (score = 0) → entre **2^1 (2)** et **2^6 (64)**
- Plus le score augmente → nombres plus **grands** et jeu plus **difficile **
