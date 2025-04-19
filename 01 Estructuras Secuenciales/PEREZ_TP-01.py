# Ejercicio 1
 
print(f"Hola Mundo!")

# Ejercicio 2

nombre = input("Por favor, ingrese su nombre:")

print(f"Hola " + nombre + "!")

# Ejercicio 3

nombre = input("Por favor, ingrese su nombre:")
apellido = input("Por favor, ingrese su apellido:")
edad = input("Por favor, ingrese su edad:")
residencia = input("Por favor, ingrese su lugar de residencia:")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4

import math

radio = float(input("Por favor, ingrese el radio de un círculo"))
perimetro = 2 * math.pi * radio

print("El perímetro del círculo es:", perimetro)

# Ejercicio 5

segundos = int(input("Ingrese la cantidad de segundos que desee: "))
horas = segundos / 3600

print(f"Los segundos equivalen a {horas} horas")

# Ejercicio 6

numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar de {numero}")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

# Ejercicio 7

numero = int(input("Ingrese un número: "))
suma = numero + numero
resta = numero - numero 
multiplicacion = numero * numero
division = numero / numero

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# Ejercicio 8

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = peso / (altura ** 2)

print(f"Su índice de masa corporal es de: {imc:.2f}")

# Ejercicio 9

gradosC = float(input("Ingrese la temperatura en Celcius: "))
gradosF = (9/5) * gradosC + 32

print(f"La temperatura en Fahrenheit es: {gradosF:.2f}°F")


# Ejercicio 10

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")