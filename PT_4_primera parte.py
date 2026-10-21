registros = 0
total_personas = 0

cantidad = int(input("cantidad: "))

while cantidad != 0:
    if cantidad < 0:
        print("error: no se admite cantidad negativa.")
    else:
        registros = registros + 1
        total_personas = total_personas + cantidad 
    cantidad = int(input("cantidad: "))

print("registros realizado:", registros)
print("total de personas:", total_personas)
