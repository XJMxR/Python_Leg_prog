from module1 import * 
######################################################
# print("hello, word")
# sNombre = input("how is your name?")
# iNacimiento = int(input("en que año naciste?"))
# edad = 2023 - iNacimiento
# #print(sNombre)
# #print(edad)
# print(f"Te llamas {sNombre} y tienes {edad} años")
#######################################################

fSalario = float(input("Cual es tu salario mensual?"))
iAntiguedad =int(input("cuantos años llevas en la empresa actual"))
fSaldo = float(input("cual es el saldo en tu cuenta?"))
bReportado = bool (input("está reportado en data credito? (1=si, 0=no)"))
fValor = float(input("cuanto quiere que le preste?"))
darPrestamo = OtorgarPrestamo(fSalario, iAntiguedad, fSaldo, bReportado, fValor)
print(f"Otorgar prestamo: {darPrestamo}")

