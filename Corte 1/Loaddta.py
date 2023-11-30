def Loaddta(fileName):
    dataset=[]
    with open (fileName,encoding='utf-8') as f:
        for line in f: #iteracion reglon por reglon del archivo
            valores=line.split(sep=';')
            print(valores)
            registro = {"nombre":valores[0],
                        "direccion":valores[1],
                        "hectareas":float(valores[2]),
                        "aves":int(valores[3]),
                        "flora":int(valores[4]),
                        "estado":valores[5]} 
            dataset.append(registro)
    return dataset