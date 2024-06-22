import os
os.system("cls")

"""
Crear un crud de ventas para plantas.
"""

plantas= [
    ["cactus","verano",1,1500,50],
    ["vepl01","Cactus",1500,50],
    ["vefl02","Tulipanes"]

]

def buscar_planta(concepto):
    for a in plantas:
        if a[0].find(concepto)== 0:
            lista=[]
            lista.append(a)
        return lista
            
        #elif concepto[1].find("in") == 1:

        #elif concepto[1].find("ot") == 1:

        #elif concepto[1].find("pr")== 1 :
        
        

x=input("Ingrese que tipo de planta va a buscar: ")
coso=buscar_planta(x)
for b in coso:
    print(b)