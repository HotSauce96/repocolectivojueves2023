controlador = 100

print("****EMPANADAS EL MACHETICO****")
print("1. Agregar un sabor de empanada")
print("2. ver el sabor de empanada registrada")
print("3. SALIR")

while controlador !=3:
    controlador = int(input("Elija una opcion: "))
    if controlador == 1:
        saborEmpanada = input("Ingrese el nombre del sabor de empanada: ")
        print(f"El sabor de empanada que agregaste es {saborEmpanada}")
    elif controlador == 2:
        print(f"El sabor de la empada que registraste anteriormente es {saborEmpanada}")
    elif controlador == 3:
        print("Elegiste la opción 3 que es para salir")
    else:
        print("Opción invalida")
        
        
    
 