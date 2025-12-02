#Esercizio Pratico
# Definisco un parametro normale (che sarà la lista)
def media(numeri):
    # Calcolo somma diviso lunghezza
    return sum(numeri) / len(numeri)
# Passo una LISTA (con le parentesi quadre)
print(media([2, 4, 6]))

#Esercizio Pratico 2

#Aggiungere un nuovo contatto (nome, numero , email).
rubrica = []
#----------Funzione per nuovo contatto -------
def aggiungi_contatto(nome, numero, email):
    contatto = {
        'nome': nome,
        'numero': numero,
        'email': email
    }
    rubrica.append(contatto)
    print(f"Contatto {nome} aggiunto.")

#---------FUNZIONE PER MODIFICARE ----------- 
def modifica_contatto(nome, nuovo_numero=None, nuova_email=None):
    for contatto in rubrica:
        if contatto['nome'].lower() == nome.lower():
            if nuovo_numero:
                contatto['numero'] = nuovo_numero
            if nuova_email:
                contatto['email'] = nuova_email
            print(f"Contatto {nome} modificato.")
            return
    print('contatto non trovato')

#------------ FUNZIONA PER ELIMINARE ---------------
def elimina_contatto(nome):
    for contatto in rubrica: 
        if contatto['nome'].lower() == nome.lower():
            rubrica.remove(contatto)
            print(f'contatto {nome} eliminato')
            return
    print('contatto non trovato')

#-----------FUNZIONA PER CERCARE ----------------
def cerca_contatto(nome):
    for contatto in rubrica:
        if contatto['nome'].lower() == nome.lower():
            print('contatto trovato')
            return
    print('contatto non trovato')
    

#-------------FUNZIONE PER MOSTRARE --------
def mostra_contatti() :
    if not rubrica:
        print('Rubrica vuota')
        return
    ordinati = sorted(rubrica, key=lambda x:x ['nome'].lower())
    for contatti in ordinati :
        print(f"{contatti['nome']} - {contatti['numero']} - {contatti['email']}")


aggiungi_contatto('luca', '5628762875278', 'luca@gmail.com')
aggiungi_contatto('anna', '4998478979899', 'anna@ghaha.com')
mostra_contatti()

modifica_contatto('luca', nuova_email='luca@hhhh.it')
cerca_contatto('Anna')
elimina_contatto('Anna')
mostra_contatti() 
