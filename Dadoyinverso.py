print("-------------------------------------------")
print("----------- NUMERO INVERSO DEL DADO ----------------")
print("-------------------------------------------")
# input
Numero_dado= int(input("Digite el número del dado= "))
# processing
x = 7 - Numero_dado
if 0<Numero_dado<=6:
    rta= "El numero inverso del dado " + str(Numero_dado) + " es " + str(x)
else: 
    rta = "El numero no es de una cara de 6"

    # output
print("-------------------------------------------")
print("-------------EL RESULTADO ES---------------")
print(rta)
print("-------------------------------------------")