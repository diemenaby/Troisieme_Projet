"""" Question 1
Écrivez un programme Python qui multiplie tous les éléments d’une liste.
Liste d'échantillons = [2, 3, 6]
Résultat = 36
"""
print("Résolution de la question 1")
liste_multiples = [2, 3, 6]
listes_totales = liste_multiples[0] * liste_multiples[1] * liste_multiples[2]
print(listes_totales)
print("")
print("Fin")
print("---------------------------------")
"""
       Question 2
       
       Écrivez un programme Python pour obtenir une liste, triée par ordre croissant par le dernier élément de 
       chaque tuple, à partir d'une liste donnée de tuples non vides.
       
       Liste d'échantillons : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
       
       Résultat attendu : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
       
       Astuce : vous pouvez utiliser la fonction de tri.
       
"""
print("Résolution de la question 2")

listes_tries = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

listes_tries.sort(key=lambda trie: trie[1])
for value in listes_tries:
    print([value], end=", ")

print("")
print("Fin")
print("---------------------------------")
"""
Question 3 

Écrivez un programme Python qui combine deux dictionnaires en ajoutant des valeurs pour les clés communes.

d1 = {'a': 100, 'b': 200, 'c': 300}

d2 = {'a' : 300, 'b' : 200, 'd' : 400}

Résultat attendu : {'a' : 400, 'b' : 400, 'd' : 400, 'c' : 300}
"""
print("Résolution de la question 3")
import collections

d1 = {'a': 100, 'b': 200, 'c': 300}

d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = [d1, d2]
compter = collections.Counter()
for d in d3:
    compter.update(d)

result = dict(compter)
print()
print("Résultat attendu : ", result)

print()
print("Fin")
print("---------------------------------")
"""
Question 4
Avec un nombre entier n donné, écrivez un programme pour générer un dictionnaire 
qui contient (i, i*i) de sorte que soit un nombre entier compris entre 1 et 
n (les deux inclus). Le programme doit ensuite imprimer le dictionnaire. 
Supposons que l'entrée suivante soit fournie au programme : 8. 
La sortie doit alors être : {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25, 6 : 36, 7 : 49, 8 : 64}
"""
print()
print("Résolution de la question 4")
Entrer_Nombre = int(input("Veiller saisir un entier s'il vous plait :"))
Entrer_Nombre = Entrer_Nombre + 1
Nombre_Saisi = {Nombre: Nombre ** 2 for Nombre in range(1, Entrer_Nombre)}
print(Nombre_Saisi)
print()
print("Fin")
print("---------------------------------")
"""
Question 5

Écrivez un programme pour trier un tuple par son élément float.

Par exemple : liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

Résultat attendu : [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""
print()
print("Résolution de la question 5")
liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(liste, reverse=True))

print()
print("Fin")
print("---------------------------------")

"""
Question 6

Écrivez un programme Python pour créer un ensemble.

Exemples : {0, 1, 2, 3, 4}

Écrivez un programme Python pour effectuer une itération sur des ensembles.

Écrivez un programme Python pour ajouter des membres à un ensemble et pour supprimer des éléments d'un ensemble donné.

"""
print()
print("Résolution de la question 6")
ensemble = {0, 1, 2, 3, 4}
for value in ensemble:
    print(value, end=", ")
ajout = int(input("Veiller saisir un entier s'il vous plait :"))
ensemble.add(ajout)
print(ensemble)
supprimer = int(input("Veiller supprimer un entier s'il vous plait :"))
ensemble.remove(supprimer)
print(ensemble)

print()
print("Fin")
print("---------------------------------")
