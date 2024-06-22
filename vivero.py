
import os
from datetime import date
from datetime import datetime


os.system("cls")
date=datetime.now()
fecha=date.strftime("%Y-%m-%d")
folio=1110
productos=[]
#        folio    fecha   id ,cantidad,precio
ventas=[]
def input_id():
        while True:
            id=input("Ingrese el número de id: ")
            if len(id)==4:
                return id
            else:
                print("Error, ID debe contener cuatro caracteres.")

def suma_total_ventas():
    a=0
    for venta in ventas:
        a+=venta[4]
    return a     
def buscar_plantas(id):#muestra la planta asignada a la ID
    try:
       for i in productos:
            if i[0] == id:
                return i
    except:
       return -1
def buscar_plantas_ind(id):#busca indice de a planta por id
    a=0
    try:
        for i in productos:
            if i[0]==id:
                return a
            else:
                a+=1
    except:
        return -1
def buscar_ventas(fecha):#busca la venta en la fecha en específico.
    try:
       for i in ventas:
            if i[1] == fecha:
                return i
    except:
       return -1
def cargar_productos():
    lista=[]
    with open ("productos.txt",'r') as file:
            for linea in file:
                linea = linea.strip()
                datos = linea.split(',')
                lista.append([datos[0],datos[1],datos[2],datos[3],int(datos[4]),int(datos[5])])
            return lista
def carga_ventas():
    lista=[]
    with open ("ventas_prod.txt",'r') as file:
        for linea in file:
            linea=linea.strip()
            dats=linea.split(',')
            lista.append([int(dats[0]),dats[1],dats[2],int(dats[3]),int(dats[4])])
        return lista
opcion=0
while opcion<=4:
    print("""
                Sistema de Ventas
        --------------------------------
        1. Vender productos
        2. reportes.
        3. Mantenedores
        4. Administración
        5. Salir
          """)
    opcion=int(input("Ingrese una opción entre 1-5: "))

    match opcion:
        case 1: 
            puerta=True
            while puerta:
                os.system("cls")
                print("Espacio de compra\n\n")
                id_compra=input("indique la  id del producto comprara: ")
                venta=buscar_plantas(id_compra)
                print(venta)
                n_compra=int(input("Ingrese la cantidad que comprará: "))
                
                if venta[4]>= n_compra:
                    precio=n_compra*venta[5]
                    print(f"el total será {precio}")
                    option=True
                    while option:
                        if puerta==False:
                            break
                        else:
                            puerta1=input("Desea confirmar la compra? (si/no)")
                            if puerta1.lower()== "si":
                                folio+=1
                                ventas.append([folio,fecha,venta[0],n_compra,precio])
                                venta[4]=venta[4]-n_compra
                                print("Compra realizada con éxito")
                                os.system("pause")
                                decision=input("Desea seguir comprando? (si/no)")
                                if decision.lower()=="si":
                                    break
                                else:
                                    option=False
                                    puerta=False
                                    break
                            elif puerta1.lower()=="no":
                                print("cancelando compra.")
                                os.system("pause")
                                puerta2=input("Desea continuar la compra? (si/no) ")
                                if puerta2.lower()=="si":
                                    break
                                elif puerta2.lower()=="no":
                                    puerta=False
                                    option=False
                                    break
                                    
                        
                    if puerta==False:
                        break
                else:
                    print("Error, stock no tiene reservas")
    
        case 2:
            os.system("cls")
            op=0
            while op<=4:
                print("""
                      1.- General de ventas (con total)
                      2.- Ventas por fecha especifica (con total)
                      3.- Ventas por rango de fecha (con total)
                      4.- Salir al menu principal""")
                op=int(input("ingrese una opcion 1-4 "))
                match op:
                    case 1:
                        for i in ventas:
                            print(i)
                            print()
                    case 2:
                        for i in venta:
                            if venta <=1:
                                print(f"su compra es {venta}")
        case 3: 
            os.system("cls")
            op=0
            while op<=6:
                print("""
                        Mantenedor de productos
                    -------------------------------
                    1. Agregar
                    2. Buscar
                    3. Eliminar
                    4. Modificar
                    5. Listar
                    6. Salir al menú principal
                    """)
                op=int(input("Ingrese la opción (1-6): "))
            
                match op:
                    case 1:#agregar una planta (Falta el controlador que modera el ingreso de la id, stock y precio)
                        print("\n Agregar Planta/Flor\n")
                        print("\nAgregar datos al inventario\n")
                        id=input("Ingrese el id: ")
                        nombre=input("Ingrese el nombre de la planta: ")
                        tmp=input("Ingrese a que tamporada pertenece la planta: ")                        
                        dificultad=(input("Ingrese dificultad de la planta/flor:  "))
                        cantidad=int(input("Ingrese la cantidad de a de existencias: "))
                        precio=int(input("Ingrese el precio de la planta: "))
                        productos.append([id,nombre,tmp,dificultad,cantidad,precio])
                        os.system("cls")
                        print("Perfecto, se ha agregado nuevo producto.")
                        os.system("pause")
                    case 2:#buscar una ID (Falta controlador que modera el largo de la ID ingresada)
                        id=input_id()

                        i= buscar_plantas(id)

                        if i != -1:
                            print("Planta encontrada")
                            print(i)
                            os.system("pause")
                        else:
                            print("Error, planta no encontrada")
                            os.system("pause")
                    case 3:#
                        id=input_id()

                        i= buscar_plantas_ind(id)

                        if i != -1:
                            print(f"id encontrado en el índice {i}")
                            productos.pop(i)
                            print("Listo, datos eliminados")
                        else:
                            print("Error, planta no encontrada")
                    case 4:
                        print("\n Modificar\n")
                        id=input_id()
                        lista=buscar_plantas(id)
                        print(lista)
                        os.system("pause")
                        print("\n")
                        tmp=input("Ingrese a que tamporada pertenece la planta: ")
                        nombre=input("Ingrese el nombre de la planta: ")
                        dificultad=(input("Ingrese dificultad de la planta/flor:  "))
                        cantidad=int(input("Ingrese la cantidad de a de existencias: "))
                        precio=int(input("Ingrese el precio de la planta: "))
                        os.system("cls")
                        lista[2]=tmp
                        lista[1]=nombre
                        lista[3]=dificultad
                        lista[4]=cantidad
                        lista[5]=precio
                        ("\n------------\n")
                        print("Perfecto, se ha agregado nuevo producto.")
                        os.system("pause")
                    case 5:
                        for i in productos:
                            print(i)
                        os.system("pause")
                    case 6:break
        case 4: 
            opc=0
            while opc<=3:
                os.system("cls")
                print("""
Menú de administración
----------------------
1. Cargar datos
2. Respaldar datos (Grabar/actualizar)
3. Salir""")
                opc=int(input("Ingrese la opción que quiere realziar: "))
                match opc:
                    case 1: #se cargan los datos desde la base de datos
                        if (len(productos)) == 0:
                            lista_fantasma=cargar_productos()
                            for productonuevo in lista_fantasma:
                                productos.append(productonuevo)
                            print("Carga de productos realizada con exito.")
                            os.system("pause")
                        else:
                            print ("Error, ya hay productos cargados en el sistema")
                            os.system("pause")
                        if (len(ventas))==0:
                            lista_fantasma=carga_ventas()
                            for fechanueva in lista_fantasma:
                                ventas.append(fechanueva)
                            print("Carga de fechas realizada con exito.")
                        else:
                            print("Error, ya hay fechas en el sistema")
                    case 2:pass
#                        open with ("productos","w") as file:
#                            for productorespaldo in l
                    case 3:
                        break
                        
                
        case 5:break