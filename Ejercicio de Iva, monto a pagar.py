articulo = input("ingresa el nombre del articulo: ")
can = int(input("ingresa la cantidad del articulo: "))
precio = float(input("ingresa el precio del articulo:"))

if precio * can <= 1000:
    siva = (precio * can)/1.15
    IVA = precio * 1.15
    precioIVA = precio + IVA
    print ("el nombre del articulo:", articulo, "el precio sin IVA:", siva, "su IVA es", IVA, "y el precio despues del IVA es: ", precioIVA)
else:
    siva = (precio * can)/1.15
    IVA = precio 
    precioIVA = precio + IVA
    print ("el nombre del articulo:", articulo, "el precio sin IVA:", siva, "su IVA es", IVA, "y el precio despues del IVA es: ", precioIVA)
