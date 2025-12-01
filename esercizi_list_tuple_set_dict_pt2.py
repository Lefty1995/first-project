#esercizio 1
tuples = [(1, 3), (2, 1), (5, 0)]
ordinata = sorted(tuples, key = lambda x : x[1])
print("Tuple ordinate per il secondo elemento:", ordinata)

#esercizio 2
t = (1, 2, 3, 4, 5, 6)
pari = tuple ([ x for x in t if x % 2 == 0 ])
print("Tuple con solo numeri pari:", pari)

#esercizio 3
t = (1, 2, 3, 4)
invertita = tuple(reversed(t))
print("Tuple invertita:", invertita)

#esercizio 4
s = "programmazione"
t = tuple (set(s))
print("Tuple con caratteri unici dalla stringa:", t)

#esercizio 5
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print("Lista di coppie create con zip:", zipped)

#esercizio 6
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
c = {7, 8}
differenza = A ^ B ^ c
print("Differenza simmetrica tra i set:", differenza)

#esercizio 7
frase = 'ciao come stai ciao tutto bene'
uniche = set(frase.split())
print("Parole uniche nella frase:", uniche)

#esercizio 8
liste =[[1, 2, 3], [3, 4, 5], [6, 7, 8, 9]]
unione = set().union(*map(set, liste))
print("Unione di tutti gli elementi nelle liste:", unione)  


