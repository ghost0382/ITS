# ESPERIMENTO 2: Due etichette sullo stesso identico oggetto
# Obiettivo: Verificare che 'b = a' non copia il valore, ma attacca una seconda etichetta!

a = 500
b = a

print(f"Valore di a: {a} | ID: {hex(id(a))}")
print(f"Valore di b: {b} | ID: {hex(id(b))}")
print(f"a e b puntano allo stesso identico oggetto? -> {a is b}")

b = 600
print(f"Nuovo valore di b: {b}             | Nuovo ID: {hex(id(b))}")
print(f"Valore di a (rimasto intatto): {a} |  ID di a: {hex(id(a))}")
