# c################################################
from module1 import *
# nombre=input(" cual es su nombre?\n")
# iNacimiento=int(input("En que año nacistes\n"))
# edad = 2023 - iNacimiento
# #print("su nombre es  "+nombre)
# #print ("su edad\n",edad)
# print(f"Te llamas {nombre} y tiene {edad} años")
################################################
# Salario=float(input("Cuanto ganas Actualmente\n")),
# Antiguiedad=int(input("cuanto tiempo llevas trabajando en tu empresa actual\n")),
# SaldoBancario=float(input("cual es el saldo de tu cuenta\n")),
# Report=bool(input("esta reportado\n")),
# ValorSolic=float(input ("cuanto quiere\n")),
# Dar=Ortograr_Prestamo(Salario,Antiguiedad,ValorSolic,SaldoBancario,Report)
# print(f"otorgar prestamo:\n",Dar)

listaprueba=[1,2,3,4,5,6,7]

listaprueba2=["Hambre","Miseria","Dolor","Sufrimiento","Pena"]
listaMisc = [True,"Diego",1.60,58,listaprueba]


# varfuncion=float(input("ingrese un numero \n"))
# varfuncion2=input("Su texto\n")
# tipofuncion=input("al cuadrado/convertir A mayusculas o al cubo/convertir A minusculas ?\n")

listaconvertida=list(map(mayus,listaprueba2))

# if tipofuncion == "1":
#     funcionusar = pow2
#     funcionusar2 = convertirAmayusculas
# else :
#     funcionusar = pow3
#     funcionusar2 = convertirAminusculas

print("resultado:\n")
# print(funcionusar(varfuncion))
# print(funcionusar2(varfuncion2))
print(mayus(listaconvertida))