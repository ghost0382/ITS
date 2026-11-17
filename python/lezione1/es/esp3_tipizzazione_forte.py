# ESPERIMENTO 3: Tipizzazione Forte (Python non è JavaScript!)
# Obiettivo: Vedere come Python rifiuta le somme ambigue tra testo e numeri.

testo = "10"
numero = 5

print(f"Tipo di testo: {type(testo)} | Tipo di numero: {type(numero)}")

print("\nProviamo a fare: testo + numero ...")
try:
    risultato = testo + numero
    print("Risultato:", risultato)
except TypeError as errore:
    print("💥 BLOCCATO DALL'INTERPRETE PYTHON!")
    print("   Dettaglio errore:", errore)
    print("   Spiegazione: Python protegge i dati e non converte da solo '10' in numero o 5 in stringa!")

risultato = testo + numero
print("Risultato:", risultato)

    