#Esercizio 1
a = 10 
b = 30
print(a > b)  # False
print(a < b)  # True
print(a >= b) # False 
print(a <= b) # True
print(a == b) # False
print(a != b) # True

#Esercizio 2
x = 5
y = 15
print((x < 10) and (y > 10))  # True
print((x > 10) and (y > 10))  # False
print((x < 10) or (y < 10))   # True
print((x > 10) or (y < 10))   # False
print(not(x < 10))            # False
print(not(y > 10))            # False

#Esercizio 3
a = [1, 2, 3]
b = a 
c = [1, 2, 3]
print(a is b)  # True
print(a is c)  # False
print(a == c)  # True
print(a is not c)  # True
print(a != c)     # False

#Esercizio 4
nomi = ["Alice", "Bob", "Charlie"]
print("Alice" in nomi)    # True
print("David" in nomi)    # False

#Verifica se la persona può guidare (età ≥ 18 e patente sì)
eta = int(input("Quanti anni hai? "))
patente = input("Hai la patente? (si/no) ")
puo_guidare = eta >= 18 and patente.lower() == "si"
print(puo_guidare)

#Verifica se l'utente può entrare in biblioteca (non in ritardo o abbonamento premium)
ritardo = bool(int(input("Sei in ritardo con la restituzione dei libri? (0=no, 1=sì): ")))
premium = bool(int(input("Hai un abbonamento premium? (0=no, 1=sì): ")))
puo_entrare = not ritardo or premium
print(puo_entrare)
