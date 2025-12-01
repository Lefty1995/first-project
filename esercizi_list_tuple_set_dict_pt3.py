#esercizio 1
A = {'Anna', 'Luca', 'Marco'}
B = {'Luca', 'Giulia', 'Sara'}
print("Entrambi:", A & B)
print('Solo in A:', A - B)
print('Solo in B:', B - A)
print('totale unici:', A | B)

#esercizio 2
import random 
numeri = {random.randint(1, 100) for _ in range(20)}
print("Numeri generati:", numeri)

#esercizio 3
frase = "il gatto e il cane sono amici il gatto gioca con il cane"
parole = frase.split()
conteggio = {}
for parola in parole:
    conteggio[parola] = conteggio.get(parola, 0) + 1
print("Conteggio delle parole:", conteggio)

#esercizio 4
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
inversione = {v: k for k, v in d.items()}
print("Dizionario invertito:", inversione)


