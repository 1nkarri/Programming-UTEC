# Escribe un programa en Python que permita ingresar un monto en soles
# y muestre su equivalente en dolares y euros

coins = float(input("Ingrese la cantidad de soles a convertir: "))

dolars = 3.87 * coins
euros = 3.86 * coins

print(f"La cantidad ingresada es s/{coins} y en dolares es ${dolars} y en euros son {euros}")