import csv

# Scrittura
with open("studenti.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["nome", "eta", "corso"])
    writer.writerow(["Mario", "20", "Informatica"])
    writer.writerow(["Anna", "22", "Matematica"])
    writer.writerow(["Luca", "19", "Fisica"])

# Lettura normale
with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Lettura con DictReader
with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"nome: {row['nome']}, corso: {row['corso']}")

# Filtra solo Informatica
with open("studenti.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["corso"] == "Informatica":
            print(f"nome: {row['nome']}, corso: {row['corso']}")

# Crea maggiorenni.csv
with open("studenti.csv", "r", encoding="utf-8") as f_in, \
    open("maggiorenni.csv", "w", newline="", encoding="utf-8") as f_out:
    reader = csv.DictReader(f_in)
    writer = csv.DictWriter(f_out, fieldnames=reader.fieldnames or [])
    writer.writeheader()
    for row in reader:
        if int(row["eta"]) >= 18:
            writer.writerow(row)

print("Creato maggiorenni.csv con gli studenti over 18")

