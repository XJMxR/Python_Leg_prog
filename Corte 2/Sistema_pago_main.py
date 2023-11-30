
# Código importado desde el archivo sistema_pago.py
from sistema_de_pago import fl

moneda = int(input("Seleccione su moneda: 1 USD, 2 PESO \n"))
valor_c = int(input("Ingrese el valor de su compra \n"))
print(fl.tasa_cambio(moneda, valor_c))
