numeri = (12, 34, 56, 78, 90)
somma_pari = sum([n for n in numeri if n % 2 == 0 ])
print("La somma dei numeri pari è:", somma_pari)

#esercizio 2
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
senza_dup = []
for x in lista:
    if x not in senza_dup:
        senza_dup.append(x)
print("Lista senza duplicati:", senza_dup)

#esercizio 3
lista = [1, 2, 3, 4, 5]
k = 2 
rotated = lista[-k:] + lista[:-k]
print("Lista ruotata:", rotated)

#esercizio 4 
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
intersazione = [x for x in a if x in b]
print("Intersezione tra le due liste:", intersazione)

#esercizio 5
coppie = [("a", 1), ("b", 2), ("c", 3)]
diz = dict(coppie)
print("Dizionario creato dalle coppie:", diz)

#esericizio 6
tuples = [(1, 2), (3, 4), (5, 6)]
somma = sum([sum(t) for t in tuples])
print("Somma di tutti gli elementi nelle tuple:", somma)





