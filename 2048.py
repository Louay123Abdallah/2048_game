#Importation des modules nécessaires

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from numpy import array
from random import randint
from math import log2

#Fonction pour rechercher le maximum d'une liste
def maxi(l):
    m=l[0]
    for i in range(1,len(l)):
        if l[i]>=m:
            m=l[i]
    return m
#Declaration des variable global

score=0
m=array([[int()]*5]*6)
liste_score=[]


#Les régles de manipulation du score et du la matrice

def regle_somme_vertical(m):
   global score
   for j in range(5):
       for i in range(5,-1,-1):
           if m[i,j]==m[i-1,j]:
               m[i-1,j]*=2
               score+=m[i-1,j]
               m[i,j]=0
               
def regle_somme_horizontal(m):
    global score
    for i in range(6):
       for j in range(4):
           if m[i,j]==m[i,j+1]:
               m[i,j+1]*=2
               score+=m[i,j+1]
               m[i,j]=0

def regle_zero_vertical(m):
    for j in range(5):
        b=False
        while not b:
            b=True
            for i in range(5):
                if m[i,j]==0 and m[i+1,j]!=0:
                    m[i,j]=m[i+1,j]
                    m[i+1,j]=0
                    b=False
               
def regle_zero_horizontal(m):
    for i in range(6):
        b=False
        while not b:
            b=True
            for j in range(4):
                if m[i,j]!=0 and m[i,j+1]==0:
                    m[i,j+1]=m[i,j]
                    m[i,j]=0
                    b=False
                    
#L'ordre des régles
                    
def apply_regle(m):
    regle_zero_vertical(m)
    regle_somme_vertical(m)
    regle_zero_horizontal(m)
    regle_somme_horizontal(m)
    regle_zero_vertical(m)
    regle_zero_horizontal(m)
    
#Remplir la matrice initiale
    
def remplir(m):
    for i in range(5):
        for j in range(5):
            m[i,j]=2 ** randint(1,6)
    for i in range(5):
            m[5,i]=0
            
#Afficher la matrice initiale dans l'interface

def remplir_matrice_initial():
    remplir(m)
    for i in range(6):
        for j in range(5):
            fen.mat.setItem(i,j,QTableWidgetItem(str(m[i,j])))
            
#Afficher la matrice(aprés la manipulation des régles) dans l'interface
            
def remplir_matrice():
    for i in range(6):
        for j in range(5):
            fen.mat.setItem(i,j,QTableWidgetItem(str(m[i,j])))
            
#Récupérer la matrice depuis l'interface
            
def remplir_a_partir_QTableWidgetItem():
    for i in range(6):
        for j in range(5):
            m[i,j]=int(fen.mat.item(i,j).text())
            
#Vérifier la position saisie par l'utilisateur
            
def verif_position(m,po,a):
    if not 0<=po<=4:
        return False
    elif fen.mat.item(5,po).text()=="0" or fen.mat.item(5,po).text()==str(a):
        return True
    else:
        return False
    
#L'ajout du l'entier a dans la matrice selon les conditions
    
def jouez():
    global pn
    pn=fen.pn.text()
    if not(pn.isdecimal() and verif_position(m,int(pn)-1,a)):
        QMessageBox.critical(fen,"Erreur!","position non valide")
    elif str(a)==fen.mat.item(5,int(pn)-1).text():
        fen.mat.setItem(5,int(pn)-1,QTableWidgetItem(str(a*2)))
    else:
        fen.mat.setItem(5,int(pn)-1,QTableWidgetItem(str(a)))
        
# Générer l'entier a aléatoirement selon le score du l'utilisateur

def generate_number():
    global a
    if score==0:
        a=2**randint(1,6)
    else:
        x=int(log2(score))
        if x<=20:
            a=2**randint(1,6)
        else:
            a=2**randint(x-19,x-15)
    fen.ng.setText(str(a))

#Fonction de la vérification du fin du jeu
            
def lose_game(m,a):
    i=0
    v=True
    while i<=4 and v:
        if m[5,i]==0 or m[5,i]==a:
           v=False
        else:
            i+=1
    return v

#Fonction d'appel pour le lancement du jeu(une itération)

def on_press_enter():
    jouez()
    generate_number()
    remplir_a_partir_QTableWidgetItem()
    apply_regle(m)
    remplir_matrice()
    fen.pn.clear()
    fen.crs.setText(str(score))
    lose=lose_game(m,a)
    if lose:
        QMessageBox.critical(fen,"Fin de Jeu!","Jeu terminée ,poussez sur le bouton play pour rejouer")
        liste_score.append(score)
        fen.bss.setText(str(maxi(liste_score)))
        fen.mat.clear()
        fen.crs.clear()
        
#Fonction du boucle d'appel du jeu
        
def Play():
    remplir_matrice_initial()
    generate_number()
    fen.pn.returnPressed.connect(on_press_enter)
    
#Lancement de l'interface
    
app=QApplication([])
fen=loadUi("Interface_2048.ui")
fen.show()
fen.play.clicked.connect(Play)
app.exec_()
