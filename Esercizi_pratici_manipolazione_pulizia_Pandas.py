import pandas as pd
import numpy as np
import re

# =====================================================
# FUNZIONI DI SUPPORTO
# =====================================================

def flag_outlier_iqr(s: pd.Series) -> pd.Series:
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (s < lower) | (s > upper)

pattern_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# =====================================================
# ESERCIZIO 1 – DATASET CLIENTI (creazione + soluzione)
# =====================================================

# creo un dataset fittizio
df_clienti = pd.DataFrame({
    "Nome": ["Mario Rossi", "  Anna Bianchi ", "luCA verdi", "Pippo", "Giulia"],
    "Email": ["m.rossi@example.com", "annabianchi@@mail.it",
            "luca.verdi@mail.it ", "pippo#mail.com", "giulia@mail.it"],
    "Data_nascita": ["1990-05-10", "1985/12/01", "2000-07-30", None, "1995-01-15"],
    "Età": [33, 40, None, 50, 29],
    "Stipendio": [2500, 3200, 2800, None, 10000],   # 10000 per creare un outlier
    "Città": ["Roma", "milano ", "Roma", "Napoli", "Roma"]
})

# pulisci stringhe
str_cols = ["Nome", "Email", "Città"]
for c in str_cols:
    df_clienti[c] = df_clienti[c].astype(str).str.strip().str.lower()

# valida pattern email
df_clienti["email_valida"] = df_clienti["Email"].str.match(pattern_email)

# converte date e calcola età reale
df_clienti["Data_nascita"] = pd.to_datetime(df_clienti["Data_nascita"], errors="coerce")
oggi = pd.Timestamp("today").normalize()
df_clienti["Eta_reale"] = (oggi - df_clienti["Data_nascita"]).dtdays // 365

# imputa valori mancanti con media/mediana
num_cols = ["Età", "Stipendio", "Eta_reale"]
for c in num_cols:
    if df_clienti[c].isna().mean() <= 0.3:
        df_clienti[c] = df_clienti[c].fillna(df_clienti[c].mean())
    else:
        df_clienti[c] = df_clienti[c].fillna(df_clienti[c].median())

# outlier numerici
for c in ["Età", "Stipendio", "Eta_reale"]:
    df_clienti[f"{c}_outlier"] = flag_outlier_iqr(df_clienti[c])

# trasforma colonne ripetute in categoriche
df_clienti["Città"] = df_clienti["Città"].astype("category")

print("=== ESERCIZIO 1 – CLIENTI ===")
print(df_clienti, "\n")

# =====================================================
# ESERCIZIO 2 – DATASET VENDITE (creazione + soluzione)
# =====================================================

df_vendite = pd.DataFrame({
    "Prodotto": ["Laptop", "Mouse", "Laptop", "Monitor", "Mouse"],
    "Categoria": ["Informatica", "informatica ", "Informatica", "Periferiche", "informatica"],
    "Prezzo": [1200, 20, 1250, 300, 19],
    "Quantità": [1, 10, 2, 1, 100],   # 100 per avere un outlier su quantità
    "Data_vendita": ["2024-01-10", "2024-01-11", "2024-02-01", "2024-02-05", "2024-03-01"]
})

# pulizia stringhe e uniformazione categorie
df_vendite["Prodotto"] = df_vendite["Prodotto"].astype(str).str.strip().str.title()
df_vendite["Categoria"] = df_vendite["Categoria"].astype(str).str.strip().str.lower()

# conversione data e giorni dalla prima vendita
df_vendite["Data_vendita"] = pd.to_datetime(df_vendite["Data_vendita"], errors="coerce")
prima_data = df_vendite["Data_vendita"].min()
df_vendite["Giorni_dalla_prima"] = (df_vendite["Data_vendita"] - prima_data).dt.days

# outlier su prezzo e quantità
for c in ["Prezzo", "Quantità"]:
    df_vendite[f"{c}_outlier"] = flag_outlier_iqr(df_vendite[c])

# feature: ricavo totale, log prezzo, interazione quantità x mese
df_vendite["Ricavo_totale"] = df_vendite["Prezzo"] * df_vendite["Quantità"]
df_vendite["Log_prezzo"] = np.log1p(df_vendite["Prezzo"])
df_vendite["Mese"] = df_vendite["Data_vendita"].dtmonth
df_vendite["Qty_x_Mese"] = df_vendite["Quantità"] * df_vendite["Mese"]

# ottimizzazione memoria
df_vendite["Categoria"] = df_vendite["Categoria"].astype("category")
df_vendite["Prodotto"] = df_vendite["Prodotto"].astype("category")
df_vendite["Quantità"] = df_vendite["Quantità"].astype("int16")
df_vendite["Prezzo"] = df_vendite["Prezzo"].astype("float32")
df_vendite["Ricavo_totale"] = df_vendite["Ricavo_totale"].astype("float32")

print("=== ESERCIZIO 2 – VENDITE ===")
print(df_vendite, "\n")

# =====================================================
# ESERCIZIO 3 – DATASET MISTO (creazione + soluzione)
# =====================================================

df_mix = pd.DataFrame({
    "Nome": ["Mario Rossi", "Anna Bianchi", "Luca Verdi", "Pippo"],
    "Email": ["mario.rossi@mail.it", "anna.bianchi@mail.it", "lucaverdi@mail",
            " pippo@mail.com "],
    "Data_iscrizione": ["2023-01-10", "2022-12-01", "2024-02-15", "2020-06-01"],
    "Età": [33, 40, 24, 50],
    "Stipendio": [2500, 3200, 1800, 5000],
    "Città": ["Roma", "Milano", "Roma", "Napoli"],
    "Prodotto": ["Laptop", "Mouse", "Monitor", "Laptop"],
    "Categoria": ["informatica", "informatica", "periferiche", "informatica"],
    "Vendite": [5, 20, 2, 50],
    "Giorni_attivi": [30, 60, 10, 365]
})

# pulizia stringhe
for c in ["Nome", "Email", "Città", "Prodotto", "Categoria"]:
    df_mix[c] = df_mix[c].astype(str).str.strip().str.lower()

# valida email
df_mix["email_valida"] = df_mix["Email"].str.match(pattern_email)

# date e differenze temporali
df_mix["Data_iscrizione"] = pd.to_datetime(df_mix["Data_iscrizione"], errors="coerce")
oggi = pd.Timestamp("today").normalize()
df_mix["Giorni_da_iscrizione"] = (oggi - df_mix["Data_iscrizione"]).dtdays

# gestione mancanti (qui non ne abbiamo, ma facciamo comunque median)
num_cols_mix = ["Età", "Stipendio", "Vendite", "Giorni_attivi", "Giorni_da_iscrizione"]
for c in num_cols_mix:
    df_mix[c] = df_mix[c].astype("float")
    df_mix[c] = df_mix[c].fillna(df_mix[c].median())

# outlier numerici
for c in num_cols_mix:
    df_mix[f"{c}_outlier"] = flag_outlier_iqr(df_mix[c])

# feature numeriche/categoriali
df_mix["Vendite_medie_per_giorno"] = df_mix["Vendite"] / df_mix["Giorni_attivi"].replace(0, np.nan)
df_mix["Cliente_high_value"] = (df_mix["Stipendio"] > df_mix["Stipendio"].median()).astype(int)

# apply / lambda: fascia età + performance vendite
def fascia_eta(x):
    if x < 30:
        return "young"
    if x < 50:
        return "adult"
    return "senior"

df_mix["Fascia_eta"] = df_mix["Età"].apply(fascia_eta)

soglia = df_mix["Vendite_medie_per_giorno"].median()
df_mix["Performance_vendite"] = df_mix["Vendite_medie_per_giorno"].apply(
    lambda v: "alta" if v >= soglia else "bassa"
)

# tipi categorici / ottimizzazione
for c in ["Città", "Prodotto", "Categoria", "Fascia_eta", "Performance_vendite"]:
    df_mix[c] = df_mix[c].astype("category")

for c in ["Vendite", "Giorni_attivi"]:
    df_mix[c] = df_mix[c].astype("int32")
df_mix["Stipendio"] = df_mix["Stipendio"].astype("float32")

print("=== ESERCIZIO 3 – MISTO ===")
print(df_mix, "\n")

print("Info memoria dataset misto:")
print(df_mix.info(memory_usage="deep"))
