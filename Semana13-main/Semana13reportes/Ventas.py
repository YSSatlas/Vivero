import os
import pyfiglet 

os.system("cls")

fecha="13-06-2024"


def inicio_sistema():
    print(pyfiglet.figlet_format("Sistema de Ventas",justify="center"))
    print("\n\n")
    print("                                  Autores:  Susana Correa")
    print("                                            Cristián Garcia")
    print("\n\n")
    os.system("pause")

def buscar_id(id):    
    indice=0
    for prod in productos:
        print(indice,"  ",prod)
        if prod[0] == id:
            return indice
        indice=indice+1
    return -1 

folio = 10000
def get_folio():
    if len(ventas)!=0:
        elemento= len(ventas)-1
        return (ventas[elemento])[0]
    else:
        return -1   

def cargar_productos(archivo):
    
    # Abrimos el archivo en modo lectura  r  Read
    with open(archivo, 'r') as file:
              
        for linea in file:          
            linea = linea.strip()           
            datos = linea.split(',')
           
            productos.append(datos)
    return 1       

#10 productos
#          id    prod                     stock precio


productos=[
          ]


# es un número correlativo (folio=folio+1)

#         folio, fecha, id, cantidad, total
# 20 ventas
ventas=[ 
         
          
       ]

inicio_sistema()

opcion=0
while opcion<=4:
    os.system("cls")
    print("último folio: ", get_folio())

    print("""
                                         fecha: {fecha}
                                         versión v002

               SISTEMA DE VENTAS
        ------------------------------ 
        1. Vender productos
        2. Reportes.
        3. Mantenedor
        4. Administración
        5. Salir
        
        """)
    opcion=int(input("Ingrese una opción entre 1-4: "))
    
    match opcion:
 


        case 1:    
            '''
                *para todo el sistema, este NO se puede "caer", debe usar try/except 


                Validar datos para opción Ventas:
                    id,         largo 4
                    cantidad,   puede ser cualquier número, pero debe ser mayor que
                                0 (cero) y menor o igual al stock.
                    respuesta,  deber ser "s" o "n", o "si" o "no", pero NO j,t,z,p, etc.

                 - todas estas validaciones deben esar en funciones, asì las puede
                   usar en el modificar.
                 - si el ingreso es erróneo no debe avanzar, debe volver a pedir
                   el datos hasta que esté correcto.
                 - si la validación es correcta debe retornar 1 en caso contrario -1 

            '''


            while True:
                os.system("cls")
                print("    Vender Productos         \n")
                id=input("Ingrese ID: ")
                i=buscar_id(id)
                if i != -1:
                    print("Encontrado en el elemento ", i)
                    producto=productos[i]
                    print(producto[0]," ",producto[1]," ",producto[4]," ",producto[5]) 
                    cantidad= int(input("Ingrese cantidad a comprar: "))
                    if cantidad <= producto[4]:
                        print("Stock disponible!\n")
                        total=cantidad*producto[5]
                        print(f"El total a pagar por {cantidad} productos es {total}" )
                        respuesta=input("Desea realizar la compra s/n: ")
                        if respuesta.lower() == "s":
                            producto[4]=producto[4]-cantidad  #stock actualizado
                            #grabar venta
                            ret=get_folio()
                            if ret == -1:
                                ventas.append([folio,fecha,id,cantidad,total ])   
                            else: 
                                ventas.append([ret+1,fecha,id,cantidad,total ])                        
                    else:
                        print("Error, la cantidad ingresada supera el stock,")   
                respuesta=input("Desea comprar otro producto s/n: ")
                if respuesta.lower() == "n":
                    break



            '''
               Requisitos:
                           1. Se puede vender SOLO un producto y n cantidades
                              de ese producto, de acuerdo con el stock.
                           2. El usario debe confirmar la compra. si/no
                              si: grabo la venta (actualizo folio) y descuento stock
                              no: no grabar y preguntar si desea continuar si/no
                                     si: solicita datos para otra venta
                                     no: vuelve al menú principal.
                           3. La fecha debe ser la fecha del computador (sistema), debe
                              investigar el comando en python para esto.
                           4.- Una vez realizada la venta debe preguntar si desea comprar
                              algo mas o no...
                                 si: vuelve a pedir los datos para la venta
                                 no: salir al menú principa.

                           5.  Algoritmo de la venta.
                               a. ingreso el código del producto
                                  id = input("Ingrese el id del producto")
                               b. busca el còdigo y muestra los datos en la pantalla

                                  producto = buscar_id(id) 
                                  print(producto[0]," ",producto[1]...)

                               c. pregunta cuántos quiere?
                                  cantidad=int(input("Ingrese cantidad a comprar: ))
                               d. muestra el total a pagar

                                  total= cantidad * ....
                               e. preguntar si desea comprar si/no
                                    si: verifico stock, existe stock para la cantidad
                                        solicitada?  si: grabo la nueva venta y descuento stock
                                                     no: envío mensaje de error 
                               f. Preguntar si desea comprar otro producto si/no  
                                  si:  ir al paso a
                                  no:  break... volver al menú principal.


            ''' 
            



        case 2: 

            '''
              fisicos 1234567890 
               fecha  12-06-2024 
              logicos 0123456789

              dia=fecha[0:2]

               Validar datos para Reportes

               1.  Si no hay información debe aparecer un mensaje "No hay datos que mostrar".
               2.  en el caso de fecha, fecha de inicio y término, debe validar que:
                   a. largo sea igual a 10
                   b. formato dd-mm-aaaa  NO dd/mm/aa o aaaa
                   c. La fecha ingresada debe ser enviad a una función que valide
                         dia -> entre 1 y 31
                         mes -> entre 1 y 12
                         anio-> mayor que 2000
                         *en el caso del mes 2 debe validar que sean 28 o 29 dias dependiendo
                          si es bisiesto o no.
                    d. si la validación es correcta debe retornar 1 en caso contrario -1 

                nota:  Si el rango por fechas no da los resultados correctos, debe transformar la fecha
                       en datetime
            
            '''
            
            op=0
            while op<=4:
                os.system("cls")
                print("""
                                  REPORTES
                      ---------------------------------
                      1. General de ventas (con total)
                      2. Ventas por fecha específica (con total)
                      3. Ventas por rango de fecha (con total)
                      4. Salir al menú principal 
                      
                      """)
                op=int(input("Ingrese una opciòn 1-4: "))
               
                match op:
                    case 1: 
                        os.system("cls")
                        print("              Reporte General de Ventas              ")
                        print("-----------------------------------------------------\n")

                        for venta in ventas:
                            print(venta)


                    case 2: pass
                    case 3: pass
                  
                  
                if op==4:
                    break #sale del while y vuelve al while "principal" 

                os.system("pause")
        case 3: 
            '''
                 Validaciones para Mantenedor de productos

                 1. el id debe tener largo de 4 caracteres
                 2. al agregar el id NO debe estar repetido (no debe existir)
                 3. los datos de nombre, marca y otros que sean de texto NO deben 
                    estar vacíos.
                 4. el stock debe ser mayor igual que 0
                 5. el precio debe ser mayor igual que 0

                 - todas estas validaciones deben estar en funciones, asì las puede
                   usar en el modificar.
                 - si el ingreso es erróneo no debe avanzar, debe volver a pedir
                   el dato hasta que esté correcto.

            ''' 



            op=0
            while op<=6:
                os.system("cls")
                print("""
                          MANTENEDOR DE PRODUCTOS
                      ---------------------------------
                      1. Agregar
                      2. Buscar
                      3. Eliminar
                      4. Modificar
                      5. Listar
                      6. Salir al menú principal 
                      
                      """)
                op=int(input("Ingrese una opciòn 1-6: "))

                match op:
                    case 1: pass
                    case 2: pass
                    case 3: pass
                    case 4: pass
                    case 5: 
                        os.system("cls")
                        print("       Listado de Productos          ")
                        print("-------------------------------------\n")

                        for prod in productos:
                            print(prod)
                if op==6:
                    break #sale del while y vuelve al while "principal"    

                os.system("pause")

        case 4: 

            cargar_productos("productos.txt") 

            print("lista la carga de productos")   

            os.system("pause")
            '''
                     MENU ADMINISTRACION

                1. Cargar datos    
                2. Respaldar datos (Grabar Actualizar)
                3. Salir


                cargar datos:  Esto lee todo lo que contienen los archivos Productos.txt y
                               ventas_prod.txt y carga las lista productos y ventas.

                Respaldar datos:  Esta opción graba (actualiza) todo lo contenido en las listas
                                  productos y ventas en los archivos txt correspondientes.
            
                Observaciones:  1.  Debe tener presente que si su lista de productos y ventas
                                    ya tienen datos entonces NO debe cargar datos desde los txt.
                                    
                                     
            '''

                
    if opcion==5:
        break

print("Fin del menú")