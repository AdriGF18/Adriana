vdist = float(input("Distancia de tu casa a la escuela: "))
vherm = int(input("Hermanos: "))
vsuel = float(input("Sueldo de padres: "))

vresultado = "Si tienes beca. "

if vdist > 10 and vherm >= 2 and vsuelt <= 5000:
    print(vresultado)
else:
    vresultado = vresultado.replace("Si","No")
    print(vresultado)

              