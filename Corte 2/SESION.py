import string
import random
class Seccion_login:

    def __init__(self):
        self.user_list = {"juan": "juan123", "Pamela": "nashe123"}

    def buscarUsuario(self, nombre_usuario):
        if nombre_usuario in self.user_list:
            return nombre_usuario
        return None

    def buscarContraseña(self, contraseña):
        if contraseña in self.user_list.values():
            return contraseña
        return None
    
    def Tokens (self):
        lista_tokens=[]
        largo_str = 8
        for x in range(2):
           tokens ="".join( random.choice(string.ascii_letters + string.digits)for _ in range(largo_str))
        lista_tokens.append(tokens)
        return "token 1 ",{lista_tokens[1]}


    def L_facebook(self, usuario, contraseña):
        self.user_entrada = usuario
        self.pass_entrada = contraseña

        self.e_user = self.buscarUsuario(self.user_entrada)
        self.e_pass = self.buscarContraseña(self.pass_entrada)

        if self.user_entrada == self.e_user and self.pass_entrada == self.e_pass:
            return "Este usuario y contraseña es correcto"
        else:
            return "Usuario y/o contraseña incorrecto"

    def L_google(self, usuario, contraseña):
        self.user_entrada = usuario
        self.pass_entrada = contraseña

        self.e_user = self.buscarUsuario(self.user_entrada)
        self.e_pass = self.buscarContraseña(self.pass_entrada)

        if self.user_entrada == self.e_user and self.pass_entrada == self.e_pass:
            return "Este usuario y contraseña es correcto"
        else:
            return "Usuario y/o contraseña incorrecto"


        
