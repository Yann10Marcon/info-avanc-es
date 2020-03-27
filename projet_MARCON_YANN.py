import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

identifiant = {}
mat = {}
classes = []
def decision(ide, identifiant = identifiant) :
        if ide in identifiant:
            return "L'élève est déjà inscrit"
        else :
            print("Commencer l'inscription !")

class verif_personne:
    def __init__(self, prenom, nom, sexe):
        reponse = False
        self.prenom = prenom
        self.nom = nom
        self.sexe = sexe
        if len(prenom)<3 or len(nom)<3 or (sexe != "F" and sexe != "H"):
            reponse = True
        print(reponse)
    
    '''def accepte(self, prenom, nom):
        print('Les coordonnées de ', prenom, " ", nom, "ont été enregistrées ! ")'''

def classe(filiere, num_classe):
    return filiere+num_classe        

def matiere(classe, mat = mat):
    filiere = ""
    n = ["1","2","3","4","5","6","7","8","9","0"]
    for i in classe:
        if i not in n:
            filiere = filiere+i
    if filiere in mat:
        print()
    else :
        n = int(input("Combien y-t-il de matières dans la filière ?"))
        matiere = []
        for i in range(n) :
            matiere.append(input("Ecrire la matiere : "))
        mat[filiere] = matiere
    return mat[filiere]

def note(matiere):
        notes = []
        for i in matiere:
            try:
                print('Entrer la note en ', i, ' : ')
                note = float(input())
                while note < 0 or note > 20:
                    print('Une note est comprise entre 0 et 20 ! Entrer la note en ', i, ' : ')
                    note = float(input())
            except (IndexError, ValueError, IndexError):
                print('Une erreur est arrivée ! Entrer la note en ', i, ' : ')
                note = float(input())   
            notes.append(note)
        return notes
    
def validation( l, n):
        if np.mean(l)<10:
            return "Non"
        else:
            return "Oui"

def moyenne_ge(classe, dic = identifiant):
    som = 0
    k = 0
    for cle in dic.keys():
        if classe == identifiant[cle][3]:
            k = k + 1
            som = som + dic[cle][6][1]
    return "Moyenne générale de la classe : ", round(som/k, 2)

def moyenne_mat(classe, liste, dic = identifiant):
    moys = []
    for i in range(len(liste)):
        som = 0
        k = 0
        for j in dic.keys():
            if classe == identifiant[j][3]:
                k = k + 1
                som = som + dic[j][5][1][i]
        moys.append(round(som/k,2))
    return "Les moyennes pour chaque matrière dans la classe :", moys

def radar(matiere, gp1, gp2):
    dv = {'group': ["L'élève","La classe"]}
    for i in range(len(matiere)):
        dv[matiere[i]] = [gp1[i],gp2[i]]
    df = pd.DataFrame(dv)
    categories=list(df)[1:]
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(0)
    plt.yticks([5,10,15], ["5","10","15"], color="grey", size=7)
    plt.ylim(0,20)
    values=df.loc[0].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="L'élève")
    ax.fill(angles, values, 'b', alpha=0.1)
    values=df.loc[1].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="La classe")
    ax.fill(angles, values, 'r', alpha=0.1)    
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.figure(1, figsize=(30, 16))
    plt.show()


def bulletin():    
    choix = True
    while choix:
        print('----------Menu-----------')
        print("1. Regarder les notes d'un élève enregistrer")
        print("2. Inscrire un nouvel étudiant")
        print("3. Quitter")
        choisir = input("Quel est votre choix ? (1, 2 ou 3) : ")
        if choisir == "1":
            if len(identifiant) == 0:
                    print("Il n'y a pas d'étudiant inscrit")
            else:        
                ide = input("Quel est l'identifiant de l'élève ? : ")
                while ide not in identifiant:
                    print("Cet étudiant n'existe pas ! ")
                    ide = input("Quel est l'identifiant de l'élève ? : ")
                    print(identifiant[ide])
        elif choisir == "2":
            ide = input("Quel est l'identifiant de l'élève ? : ")
            decis = decision(ide) 
            while decis == "L'élève est déjà inscrit":
                print(decis)
                ide = input("Quel est l'identifiant de l'élève ? : ")
                decis = decision(ide) 
            print("Entrer les coordonnées de l'élève : ")
            pre = input('Entrer son prenom : ')
            name = input('Entrer son nom :')
            sex = input('Quel est son sexe ? (F ou H): ')
            verif = verif_personne(pre, name, sex)
            while verif == True:
                verif = verif_personne(pre, name, sex)
                print("Une coordonnée n'est pas valide ! Entrer les coordonnées de l'élève : ")
                pre = input('Entrer son prenom : ')
                name = input('Entrer son nom :')
                sex = input('Quel est son sexe ? : ')   
                
            niveau = input("Quel est son niveau d'étude ? : ")
            filiere = input("Quelle est sa filière : ")
            num_classe = str(int(input("Quel est le numéro de classe : ")))
            cla = classe(filiere, num_classe)
            mat = matiere(cla)
            valeurs = note(mat)
            identifiant[ide] = [pre, name, sex, cla, niveau, ("Ses notes :", valeurs), ("Sa moyenne générale:", round(np.mean(valeurs),2)), 
                   ("L'écart-type :", round(np.std(valeurs),2)), ("Sa meilleure note", max(valeurs)), 
                   ("Sa pire note", min(valeurs)), ("Validation de son trimestre", validation(valeurs,2))]
            for cle in identifiant.keys():
                if cla == identifiant[cle][3]:
                    try:
                        identifiant[cle][11] = moyenne_ge(cla)
                        identifiant[cle][12] = moyenne_mat(cla, valeurs)
                    except IndexError:
                        identifiant[cle].append(moyenne_ge(cla))
                        identifiant[cle].append(moyenne_mat(cla, valeurs))
                    cle = cle
                moyclasse = identifiant[cle][12][1]
                print("Cet étudiant vient d'etre inscrit")
                print(identifiant[ide])
                radar(mat, valeurs, moyclasse)
        elif choisir == "3":
            choix = False
        else :
            print("Ce choix n'est pas disponible ! Une erreur vient de se passer !")
            break

#Pour lancer
bulletin()