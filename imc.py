nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese su apellido: ")

if (nombre == "" or apellidos == ""):
    print("Debe ingresar su nombre y apellidos")
    exit()

try:
    edad = int(input("Ingrese su edad en años: "))
    peso = float(input("Ingrese su peso en Kg: "))
    altura = float(input("Ingrese su altura en Metros: "))

except:
    print("Error: Ingrese solo numeros")
    exit()
imc = (peso/altura)**2



print(nombre+" " +apellidos +', su IMC es: '+ str(imc) )
