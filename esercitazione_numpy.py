import numpy as np

# Array di base
dati = np.random.randint(10, 100, size=(6, 5))
print("Dati originali:\n", dati)

print("\nShape:", dati.shape)
print("Tipo di dato:", dati.dtype)

# Indexing base
print("\nPrima riga:", dati[0])
print("\nPrima colonna:", dati[:, 0])
print("Sub-matrice (prime due righe, prime tre colonne):\n", dati[:2, :3])

# View vs copy
view = dati[:2, :2]
copy = dati[:2, :2].copy()
view[0, 0] = 999
print("\nDati originali dopo la modifica della view:\n", dati)
print("La copy resta invariata:\n", copy)

# Reshape (nota: 6*5 = 30, quindi 10x3 va bene)
reshape = dati.reshape(10, 3)
print("\nDati reshaped:\n", reshape)

# Iterazione con nditer
print("\nIterazione su ogni elemento con nditer:")
for elemento in np.nditer(reshape):
    print(int(elemento), end=" ")
print()

# Unione orizzontale
extra = np.random.randint(10, 100, size=(6, 5))
unito = np.hstack((dati, extra))
print("\nDati uniti:\n", unito)

# Split orizzontale
split = np.hsplit(unito, 2)
print("\nDati splittati:\n", split[0], "\n", split[1])

# Maschera booleana
mask = dati > 50
print("\nMaschera:\n", mask)
print("\nDati filtrati con maschera:\n", dati[mask])

# Ordinamento per righe
ordinati = np.sort(dati, axis=1)
print("\nDati ordinati per righe:\n", ordinati)

# Radici quadrate (float)
radici = np.sqrt(dati)
print("\nRadici quadrate dei dati:\n", radici)
