#Esercizio 1
numeri = {1, 2, 3, 4, 5, 1, 1, 2}
print(numeri)

#Esercizio 2
s  = {"a", "b" , "c"}
s.add("d")
print(s)

#Esercizio 3
s = {"a", "b" , "c"}
b = {"d", "e" , "c"}
print(s.union(b))
print( s | b )
print(s.intersection(b))
print( s & b )
print(s.difference(b))
print( s - b )

#Esercizio 4
s = {"mela", "arancia" , "banana"}
print("mela" in s)
print("kiwi" in s)

#Esercizio Pratico
corso_A = {"Antonio", "Enrico", "Alessia"}
corso_B = {"Enrico", "Luca", "Marco"}
print("Studenti iscritti ad entrambi i corsi:", (corso_A & corso_B))
print("Studenti iscritti al corso A ma non al corso B:",  (corso_A - corso_B))
print("Studenti iscritti al corso B ma non al corso A:", (corso_B - corso_A))
print("Studenti iscritti ad almeno uno dei due corsi:" , (corso_A | corso_B))
print("Tutti gli studenti iscritti ad entrambi i corsi:" , (corso_A.union(corso_B)))


