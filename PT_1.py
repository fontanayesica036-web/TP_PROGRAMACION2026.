precio = float(input("precio del producto: $"))
if precio < 0:
    print("error: el precio no puede ser negativo.")
else:
    if precio >= 20000:
        descuento = precio * 0.10

    else:
         descuento = 0

    total = precio - descuento
    print(f"precio original: ${precio}")
    print(f"descuento: ${descuento}")
    print(f"total a pagar: ${total}")
