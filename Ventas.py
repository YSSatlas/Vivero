import os
os.system("cls")

productos=[]

opcion=0
while opcion<=4:
    print("""
                Sistema de Ventas
        --------------------------------
        1. Vender productos
        2. reportes.
        3. Mantenedores
        4. Salir
          """)
    opcion=int(input("Ingrese una opción entre 1-4: "))

    match opcion:
        case 1: pass
        case 2: pass
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
                    case 1:pass
                    case 2:pass
                    case 3:pass
                    case 4:pass
                    case 5:pass
                    case 6:break
        case 4: break