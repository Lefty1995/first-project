#Esercizio 1
n = 9
if n % 3 == 0:
    print("Il numero inserito è multiplo di 3")
else:
    print("Il numero inserito non è multiplo di 3")

#Esercizio 2
voto = 75
if voto >= 60:
    print("Esame superato Congratulazioni!")
else:
    print("Esame non superato Riprova!")

#Esercizio 3
c = "a"
if c in 'aeiou':
    print("vocale")
else:
    print("consonante")

#Esercizio 4
n = 0
if n > 0 : 
    print("Positivo")
elif n < 0 :
    print("Negativo")
else:
    print("Zero")

#Esercizio 5
a, b, c = 5, 10, 7
if a >= b and a >= c:
    print("a è il numero più grande")
elif b >= a and b >= c:
    print("b è il numero più grande")
else:
    print("c è il numero più grande")

#Esercizio 6
eta = 5
if eta < 13:
    prezzo = 5
elif eta < 65:
    prezzo = 10
else:
    prezzo = 7  
print("Il prezzo del biglietto è:", prezzo, "euro")

#Esercizio 7
a, b, c = 3, 4, 4
if a == b == c:
    print("Triangolo Equilatero")
elif a == b or b == c or a == c:
    print("Triangolo Isoscele")
else:
    print("Triangolo Scaleno")




