# ESPERIMENTO 1: Le variabili come "Etichette" (Post-it) e non scatole
# Obiettivo: Vedere che il tipo appartiene al dato in memoria, non alla variabile 'x'.

x = 100
print("   x punta a:", x)
print("   Tipo di x:", type(x))
print("   Indirizzo di memoria (ID):", hex(id(x)))

print("\n--- Spostiamo il post-it 'x' su una stringa ---")
x = "ITS Academy"
print("   x punta a:", x)
print("   Tipo di x:", type(x))
print("   Indirizzo di memoria (ID):", hex(id(x)))


x=input('scrivi qualcosa:')
print("3. x punta a:", x)
print("   Tipo di x:", type(x))
print("   Indirizzo di memoria (ID):", hex(id(x)))
