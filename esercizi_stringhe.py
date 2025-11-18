#Esercizio 1 
testo = 'Python'
print('primo carattere: ', testo[0])
print('ultimo carattere: ', testo[-1]) 

#Esercizio 2
testo = 'Python è FanTasTicO'
print(testo.upper())
print(testo.lower())

#Esercizio 3
testo = '   Python è fantastico   '
lettera = 'a'
conteggio = testo.count(lettera)
print('Il numero di volte che la lettera', lettera, 'compare è:', conteggio ,'dalla parola originale.',testo)

#Esercizio 4
testo = 'Python è fantastico'
print(testo.startswith('P'))
print(testo.endswith('o'))

#Esercizio 5
testo = 'Python è fantastico'
print(testo[::-1])

#Esercizio 6
testo = '      Python è fantastico        '
print(testo.strip())

#Esercizio 7
testo = 'Python è fantastico'
print(testo [:6] * 3)





