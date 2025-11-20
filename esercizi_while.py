#Esercizio 1
i = 1
while i <= 5:
    print(i)
    i += 1

#Esercizio 2
i = 2
while i <= 10:
    print(i)
    i += 2

#Esercizio 3
i = 1
somma = 0
while i <= 10:
    somma += i
    i += 1
print("La somma dei numeri da 1 a 10 è:", somma)

#Esercizio 4
n = 7
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

#Esercizio 5
somma = 0
n = int(input("Inserisci un numero positivo (0 per uscire): "))
while n != 0:
    somma += n
    n = int(input("Inserisci un numero positivo (0 per uscire): "))
print("La somma dei numeri inseriti è:", somma)

#Esercizio 6
segreto = 7
tentativo = int(input("Indovina il numero segreto (tra 1 e 10): "))
while tentativo != segreto :
    tentativo = int(input("Indovina il numero segreto (tra 1 e 10): ")) 
print("Complimenti! Hai indovinato il numero segreto.")

#Esercizio 7
i = 1
while i <= 15:
    print(i)
    i += 2

    