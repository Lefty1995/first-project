#Esercizio Pratico
studente = {"nome": "Luca", "cognome": "Rossi", "età": 21, "corso": "Informatica"}
studente["numero matricola"] = "123456"
studente.get("email") 
for k in studente.keys():
    print(k)
for k , v in studente.items():
    print(f"{k}: {v}")
for v in studente.values():
    print(v)

    



    