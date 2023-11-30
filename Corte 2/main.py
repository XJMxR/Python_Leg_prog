from SESION import *


fl = Seccion_login()
usuario = fl.L_facebook("juan", "juan123")
usuario2 = fl.L_facebook("Pamela", "nash2e123")

ok = fl.Tokens()
print(usuario)
print(usuario2)
print(ok)