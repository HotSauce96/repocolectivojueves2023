

# Se crea la tupla: 

numeros = (50, 40, 41, 39, 30, 48, 87)

# Se crea listas vacías que van a almacenar los nuevos valores que cumplan con la condición


listaPares= []
listaMayores = []

#Ciclo for que recorre los valores de la tupla (numeros) y la variable i será la iteración que vaya revisando si se cumplen las condiciones. 
for i in numeros:
    if i % 2 == 0:
        listaPares.append(i)
        
for i in numeros:
        if i > 40:
            listaMayores.append(i)
    
# Por último se imprime la tupla(numeros) y las listas con nuevos valores tomados de la tupla.    
print ("De la lista de números",numeros, "Los numeros pares son: ", listaPares, "y los mayores a 40 son: ", listaMayores)

