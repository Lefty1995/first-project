# ==============================================================================
# 🐍 BIGNAMI DI PYTHON (CHEAT SHEET)
# ==============================================================================
# COME LEGGERE QUESTO FILE:
# 1. Tutto ciò che inizia con '#' è un commento (spiegazione).
# 2. Le parole tra [PARENTESI QUADRE] sono i nomi o i valori che decidi TU.
# 3. Il resto è codice fisso che devi imparare.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. LE BASI: VARIABILI E STAMPA
# ------------------------------------------------------------------------------

# Creare una variabile (Assegnazione)
# Sintassi: [NOME] = [VALORE]
eta = 25
nome = "Mario"

# Scrivere a schermo
# Sintassi: print([COSA_STAMPARE])
print(nome)
print("Ciao mondo")


# Chiedere il tipo di dato
# Sintassi: type([VARIABILE])
print(type(eta))  # Ti dirà se è int, float, str, ecc.

# ------------------------------------------------------------------------------
# 2. TIPI DI DATI E CONVERSIONE (CASTING)
# ------------------------------------------------------------------------------

numero_intero = 10        # int (numeri interi)
numero_decimale = 9.99    # float (numeri con la virgola)
testo = "100"             # str (testo, anche se contiene numeri)
booleano = True           # bool (Vero o Falso)

# Convertire i dati (Casting)
x = int("10")      # Diventa numero 10
y = float(5)       # Diventa 5.0
z = str(100)       # Diventa testo "100"

# ------------------------------------------------------------------------------
# 3. OPERAZIONI MATEMATICHE E LOGICHE
# ------------------------------------------------------------------------------

# Matematica
somma = 10 + 5
sottrazione = 10 - 5
moltiplicazione = 10 * 2
divisione = 10 / 2       # Restituisce sempre un float (es. 5.0)
potenza = 3 ** 2         # 3 alla seconda (9)
modulo = 10 % 3          # Il resto della divisione (1)

# Confronti (Restituiscono True o False)
uguale = (5 == 5)        # Attenzione: DOPPIO uguale per confrontare
diverso = (5 != 3)
maggiore = (10 > 2)
minore = (2 < 5)

# ------------------------------------------------------------------------------
# 4. STRINGHE (TESTO)
# ------------------------------------------------------------------------------

nome = "Luca"
cognome = "Rossi"

# Unire testi (Concatenazione)
completo = nome + " " + cognome

# Inserire variabili nel testo (f-string) -> CONSIGLIATO
frase = f"Ciao, mi chiamo {nome} e ho {eta} anni."

# Metodi utili
maiuscolo = nome.upper()  # "LUCA"
minuscolo = nome.lower()  # "luca"

# ------------------------------------------------------------------------------
# 5. DECISIONI (IF - ELIF - ELSE)
# ------------------------------------------------------------------------------
# Regola: I due punti ':' alla fine sono obbligatori.
# Regola: L'indentazione (spazio a destra) è obbligatoria per ciò che sta dentro.

voto = 20

if voto >= 18:
    # (TAB) Fai questo se la condizione è VERA
    print("Promosso")

elif voto >= 10:
    # (TAB) Fai questo se la prima era falsa, ma questa è VERA
    print("Rimandato")

else:
    # (TAB) Fai questo se TUTTO il resto era FALSO
    print("Bocciato")

# ------------------------------------------------------------------------------
# 6. CICLI (RIPETIZIONI)
# ------------------------------------------------------------------------------

# A) CICLO WHILE (Finché...)
# Usalo quando NON sai quante volte ripetere, ma sai la condizione.
contatore = 0

while contatore < 5:
    print(f"Giro numero {contatore}")
    # IMPORTANTE: Cambia la condizione per non bloccare il PC
    contatore = contatore + 1 

# B) CICLO FOR (Per ogni...)
# Usalo quando SAI quante volte ripetere o devi scorrere una lista.

# Esempio con numeri (range)
# range(start, stop) -> stop è escluso
for numero in range(0, 5):
    print(numero)  # Stampa 0, 1, 2, 3, 4

# Esempio con una lista
colori = ["Rosso", "Blu", "Verde"]
for colore in colori:
    print(f"Il colore è: {colore}")

# ------------------------------------------------------------------------------
# 7. LISTE (ELENCHI ORDINATI)
# ------------------------------------------------------------------------------
# Le liste usano parentesi QUADRE []

spesa = ["Pane", "Latte", "Uova"]

# Leggere
primo_elemento = spesa[0]  # Indice parte da 0!
ultimo_elemento = spesa[-1]

# Modificare
spesa[1] = "Latte di Soia" # Cambio "Latte"

# Aggiungere
spesa.append("Biscotti")   # Aggiunge in fondo

# Lunghezza
numero_oggetti = len(spesa)

# ------------------------------------------------------------------------------
# 8. DIZIONARI (CHIAVE : VALORE)
# ------------------------------------------------------------------------------
# I dizionari usano parentesi GRAFFE {}

persona = {
    "nome": "Anna",
    "eta": 30,
    "citta": "Roma"
}

# Leggere
print(persona["nome"])

# Modificare o Aggiungere
persona["eta"] = 31          # Modifica esistente
persona["lavoro"] = "Dev"    # Aggiunge nuovo

# ------------------------------------------------------------------------------
# 9. FUNZIONI (I TUOI COMANDI)
# ------------------------------------------------------------------------------

# 1. Definizione (Crei la ricetta)
def saluta_utente(nome_utente):
    messaggio = f"Ciao {nome_utente}, benvenuto!"
    return messaggio

# 2. Chiamata (Usi la ricetta)
risultato = saluta_utente("Marco")
print(risultato)