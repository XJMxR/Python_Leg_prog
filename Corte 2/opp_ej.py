class Data:
   
    #atributos de instancia(estaticos)
    numLoads=0
    #atributos de instacia
    #inicializar
    def _init_(self,filename) -> None:
            self.filename  

    def loadData(self,f):
        numLoads=numLoads+1

class Persona:
     species="Homo Sapiens"
     galaxy="Milk Way"
     average_life="75"

     def __init__(self,pNombre,pEdad,pEstatura,pPeso,pSxo):
          self.nombre=pNombre
          self.edad=pEdad
          self.estatura=pEstatura
          self.pesp=pPeso
          self.genero=pSxo
     #sobrecarga de la funcion para imprimir
     def __str__(self) -> str:
          if self.genero == "H":
                return f"{self.nombre} es un ,{self.species} de {self.edad} años que vive en la {self.galaxy}"
          else:
               return f"{self.nombre} es una mujer {self.species} de {self.edad} años que vive en la {self.galaxy}"

#clase extendidad
#Heredamiento

class Empleado(Persona):
     def __init__(self, pNombre, pEdad, pEstatura, pPeso, pSxo,pSalario,pCargo):
          #Usa la inicializacion de la clase persona, la SUPER CLASE
          super().__init__(pNombre, pEdad, pEstatura, pPeso, pSxo,pSalario,pCargo)
          self.salario=pSalario
          self.pCargo = pCargo


     
class Estudiante(Persona):
     def __init__(self, pNombre, pEdad, pEstatura, pPeso, pSxo,pCarrera,pSemestre):
          super().__init__(pNombre, pEdad, pEstatura, pPeso, pSxo,pCarrera,pSemestre)
          self.carrera=pCarrera
          self.semestre =pSemestre
          self.__prueba = False

     def __str__(self) -> str:
         super().__str__()
         return f"{self.nombre} es un ,{self.species} de {self.edad} años que vive en la {self.galaxy},de {self.carrera} y {self.semestre}"
   