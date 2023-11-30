class PayMethod:

    pass

class Conversor:
    
    def tasa_cambio(self, moneda, plata):  # 1 para USD a peso, 2 para pesos a dolar
        self.plata_c = plata
        
        if moneda == 1:
            self.plata_c = self.plata_c * 0.00024
            return f"Su valor actual en Dolares es \n {self.plata_c}$"
        
        elif moneda == 2:
            self.plata_c = self.plata_c * 4266.24
            return f"Su valor actual en Pesos es \n {self.plata_c}$"
        
        else:
            return "OPCION NO ENCONTRADA"

# Código importado desde el archivo sistema_pago.py
from sistema_pago import fl

moneda = int(input("Seleccione su moneda: 1 USD, 2 PESO \n"))
valor_c = int(input("Ingrese el valor de su compra \n"))
print(fl.tasa_cambio(moneda, valor_c))
