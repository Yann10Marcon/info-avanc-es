"""
Contrôle de connaissances
Tout est à faire en pur python respectez bien le nommage des variables

    Question 1 : Fonction
    Créer une fonction appelée sup21 qui renvoie si un nombre est supérieur ou égal à 21

    >>> sup21(21)
    True
    >>> sup21(2)
    False

    Question 2 : listes
    Créer une fonction `pairs` qui renvoie les éléments pairs d'une liste

    >>> pairs([1,2,3])
    [2]

    Question 3 : Création de fonction
    Créer une fonction 'ajout4' qui prend en paramètre une liste et
    renvoie une nouvelle liste avec l'entier 4 ajouté à la fin.
    Vous ne devez pas modifier la liste de départ

    >>> ajout4([])
    [4]
    >>> ajout4([1,2,4])
    [1, 2, 4, 4]
    >>> l = [1,2,3]
    >>> _ = ajout4(l)
    >>> l
    [1, 2, 3]

    Question 4
    Créer une fonction 'to_strings' qui pour un dictionnaire renvoie une liste de chaines de caractères
    au format suivant : 'clé:valeur'
    Exemple : pour {1:2} il faut renvoyer ['1:2']

    >>> to_strings({1:2})
    ['1:2']
    >>> to_strings({})
    []
    >>> to_strings({1:2,3:4})
    ['1:2', '3:4']

    Question5
    Créer une fonction 'extremites' qui renvoie les deux premiers et
    les deux derniers d'une liste : pour [1,2,3,4,5], renvoyer [1,2,4,5]

    >>> extremites(['a', 'b', 'c', 'd', 'e'])
    ['a', 'b', 'd', 'e']

    Question 6
    Créer une classe 'Mot' avec un attribut 'mot' et une methode 'comptelettre'
    qui prend en paramètre un caractère et renvoie le nombre d'occurences de ce
    caractère dans le mot. Attenton cela ne doit pas être sensible à la casse

    >>> mot = Mot('Bonjour')
    >>> mot.mot
    'Bonjour'
    >>> mot.comptelettre('o')
    2
    >>> mot.comptelettre('B') == mot.comptelettre('b') == 1
    True

    Question 7
    Créer une fonction 'tri_et_inverse' qui prend en paramètre une liste
    et renvoie (sans modifier la liste de départ) la liste triée et la liste départ mais dans le sens inverse

    >>> maliste = [4,7,6]
    >>> tri_et_inverse(maliste)
    ([4, 6, 7], [6, 7, 4])
    >>> maliste == [4,7,6]
    True

    Question 8: while et entrée utilisateur
    Completez fonction 'aller_a_paris' définie apres la doctest.
    Elle doit lire l'entrée utilisateur jusqu'a ce que l'utilisateur saisisse une chaine qui en
    minuscule vaut 'paris'.
    dans ce cas-là renvoyer "Paris" et le nombre de saisies utilisateur

    Pour les besoins du test j'utilise une petite astuce pour que vous n'ayez pas à saisir en vrai.

    >>> class fake_input:
    ...     def __init__(self, saisies):
    ...         self._iter = iter(saisies)
    ...     def __call__(self, *args, **kwargs):
    ...         return next(self._iter)
    ...
    ...
    >>> list(aller_a_paris(input_call=fake_input(['Barcelone', "Madrid", "Paris"]))) 
    [3, 'Paris']
    >>> aller_a_paris(input_call=fake_input(['Barcelone', "paris"]))
    (2, 'Paris')

    Question 9
    Créer un dictionnaire 'ville_nom_pays' qui contient en
    clefs 'Paris', 'Berlin', 'Madrid' et 'Moscou' et en
    valeur les noms des pays correspondants

    >>> 'Paris' in ville_nom_pays
    True
    >>> 'Espagne' in list(ville_nom_pays.values())
    True
    >>> to_strings(ville_nom_pays)
    ['Paris:France', 'Berlin:Allemagne', 'Madrid:Espagne', 'Moscou:Russie']

    Question 10
    - Créer une classe Pays dont les instances ont comme  attributs 'nom' (le nom du pays)
    et 'visa' (un visa est necessaire pour un ressortissant francais)


    >>> italie = Pays('Italie', False)
    >>> italie.visa
    False
    >>> italie.nom
    'Italie'
    
    - Créer un dictionnaire 'ville_pays' avec les capitales comme clefs et les
    instances de pays comme valeurs. Pour Paris, Berlin, Mardrid et Moscou.
    Il faut un visa pour aller en Russie.
    Il ne faut pas de visa pour aller dans les trois autres pays

    >>> ville_pays['Moscou'].visa
    True
    >>> ville_pays['Berlin'].visa
    False
    
"""
#Question 1
def sup21(nombre):
    if nombre >= 21:
        return True
    else:
        return False

#Question 2
def pairs(liste):
    pairs=[]
    for i in liste:
        if i%2==0:
            pairs.append(i)
    return pairs

#Question 3
def ajout4(liste):
    l = liste + [4]
    return l

#Question 4
def to_strings(dico):
    strings = []
    for name, number in dico.items():
        strings.append(f"{name}:{number}")
    return strings

#Question 5
def extremites(l):
    k = []
    for i in [0,1]:
        k.append(l[i])
    for i in [2,1]:
        k.append(l[-i])
    return k

#Question 6

#Question 7
def tri_et_inverse(l):
    k = []
    o = l[::-1]
    k.append(sorted(l))
    k.append(o)
    return k
#Question 8
    
def aller_a_paris(input_call=input):
    # code a remplir

    # quelque part dans le code de cette fonction: saisie = input_call('Question ')
    # en fonction de saisie on continue a demander ou on renvoie 'Paris'
    # Au lieu d'utiliser input comme en cours vous appelez input_call
    # par défaut elle vaut input donc vous pouvez appeller
    # aller_a_paris() pour tester a la main
    while True:
        return 0, 'Nulle Part'

#Question 9
ville_nom_pays = {"Paris":"France",
                  "Berlin":"Allemagne",
                  "Madrid":"Espagne",
                  "Moscou":"Russie"}

#Question 10
class Pays:
    visa = False
   
    def __init__(self, nom, visa):
        self.nom = nom
        self.visa = visa
        if nom == "France":
            visa = True
     
if __name__ == "__main__":
    import doctest
    if True:
        doctest.testmod(verbose=True, optionflags=512)
    else:
        doctest.testmod(verbose=True)

