num1 = int(input("Ingrese el primer numero:  "))

num2 = int(input("Ingrese el segundo numero:  "))

print ("Menu: ")

print ("1.- Suma")
print ("2.- Resta")
print ("3.- Multiplicacion")
print ("4.- Division")

resp = int(input("Ingrese la opcion:  "))

if resp == 1:
    resul = int(num1 + num2)
elif (resp == 2):
    resul = int(num1 - num2)
elif (resp == 3):
        resul = int(num1 * num2)
elif (resp == 4):
    if num2 == 0:
        print("No se puede dividir")
        resul = 0
    else:
        resul = int(num1 / num2)

print ("Resultado: ", resul)