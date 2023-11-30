def Ortograr_Prestamo(pSlario,
                      pAntiguiedad,
                      pSaldoBancario,
                      pReport,
                      pValorSolic ):
  #  pass
  if pSlario > 1200000 and pAntiguiedad >2 and pValorSolic <= pSaldoBancario and pReport == False:
    return True
  else:
    return False  
def funcionpura(listadentrada):
  listaout =[]

  for x in listadentrada:
      listaout.append(x**2)
      return listaout
def pow2(var):
    return var**2
def pow3 (var):
    return var**3

def convertirAminusculas(listadentrada):
  listanueva =[]
  for nombre in listadentrada:
     listanueva.append(str(nombre).lower())
  return listanueva

def convertirAmayusculas(listadentrada):
  listanueva=[]
  for nombre in listadentrada:
      listanueva.append(str(nombre).upper())
  return listanueva

def mayus(item):
   return(str(item).upper())