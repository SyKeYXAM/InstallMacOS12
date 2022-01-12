#!/usr/bin/python3
import os

print ("1. Instalar programas necesarios")
print ("2. Crear fichero BaseSystem.img")
print ("3. Crear disco")
print ("4. Instalar MacOS 12 Monterey")
print ("5. Salir")

opcion = int(input("Elige una opcion: "))

if opcion == 1:
	os.system("bash InstalarSW.sh")
elif opcion == 2:
	os.system("bash CrearBaseSystemImg.sh")
elif opcion == 3:
	os.system("bash CrearDisco.sh")
elif opcion == 4:
	os.system("bash InstalarMacOS.sh")

