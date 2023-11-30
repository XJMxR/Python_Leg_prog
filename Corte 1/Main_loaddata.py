from Loaddta import *

def filtroAves(humedal):
    return humedal["aves"]>100
def filtroH(humedal):
    return humedal["hectareas"]>=3

NombreArchivo=input("nombre de archivo\n")
miDataSet=Loaddta(NombreArchivo)
# humedal1= {"nombre":"Lago de las garzas",
#            "direccion":"carrera 127 con calle 16A",
#             "hectareas": 4.7,
#             "especies de aves":149,
#             "flora":148,
#             "estado":"en conservacion" }
# print(humedal1["nombre"]+"\n")




# datasetF=list(filter(lambda x:x ["hectareas"]>9.0 ,miDataSet))

# print(f"\nHumedales Friltados {len(datasetF)}\n")
# print("\n",datasetF)

registro = {"nombre":"PAMpalinda",
    "direccion":"calle 5 62-5",
    "hectareas":20,
    "aves":54,
    "flora":37,
    "estado":"En conservacion"} 

# campo_mayus = registro["nombre"].lower()

def fminus (idatos):

    return { idatos["nombre"],
            idatos["direccion"],
            idatos["aves"],
            idatos["flora"],
            idatos["estado"].upper()
            }

print("\n",list(map(fminus,miDataSet)),"\n")
