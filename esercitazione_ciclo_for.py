#Esercizio 1
for i in range (1,11):
 print(i)

#Esercizio 2
for i in range ( 2, 21, 2):
    print(i)

#Esercizio 3
parola = "python"
for lettera in parola:
    print(lettera)

#Esercizio 4
somma = 0
for i in range (1, 101):
    somma += i
print("La somma dei numeri da 1 a 100 è:", somma)

#Esercizio 5
for i in range (1, 11):
   print(f" 5x {i} = {5*i}")
   print(f" 2 x {i} = {2*i}")
   
#Esercizio 6
n = 5
fattoriale = 1
for i in range (1, n+1):
   fattoriale *=i
   print("Fattoriale" , fattoriale)

#Esercizio 7
parola = "programmazione"
vocali = "aeiou"
conta = 0 
for c in parola:
   if c in vocali:
      conta +=1
print("Numero di vocali in", parola, "è:", conta)

#Esercizio 8
for numero in range (1, 4):
   for j in range (1, 4):
      print(f"{numero} x {j} = {numero*j}")
print()

#Esercizio 9
for i in range (1, 11): 
   if i == 5: 
        continue
print(i)

#Esercizio 10
for i in range (1, 11):
   if i ==7:
        break
print(i)



