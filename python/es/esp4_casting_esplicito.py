# ESPERIMENTO 4: Casting Esplicito (Prendere il controllo del tipo)
# Obiettivo: Convertire consapevolmente il tipo con int() o str().


numero = 5

# 1. Vogliamo una somma matematica? Convertiamo la stringa in intero
testo = input("inserisci un numero: ")
somma_matematica = int(testo) + numero
print("1. Somma Matematica (int(testo) + numero):")
print(f"   {somma_matematica} (Tipo: {type(somma_matematica)})")

# 2. Vogliamo unire i testi? Convertiamo il numero in stringa
concatenazione = testo + str(numero)
print("\n2. Concatenazione Testuale (testo + str(numero)):")
print(f"   '{concatenazione}' (Tipo: {type(concatenazione)})")

# 3. Vogliamo unire i testi? Convertiamo il numero in stringa
concatenazione = testo + numero
print("\n2. Concatenazione Testuale (testo + str(numero)):")
print(f"   '{concatenazione}' (Tipo: {type(concatenazione)})")

