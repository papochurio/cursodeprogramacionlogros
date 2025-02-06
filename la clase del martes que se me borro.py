nombre = input("por favor, ingresa tu nombre")
edad = int(input("por favor, ingresa tu edad"))
altura = float(input("por favor, ingresa tu altuta"))
ciudad = input("por favor dime de que ciudad eres")

print(f"Hola, {nombre} tienes {edad} años, mides {altura} y eres de {ciudad} ")

a = int(input("por favor, ingresa un numero"))
b = int(input("por favor, ingresa un numero"))
c = int(input("por favor, ingresa un numero"))

if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
else:
    mayor = c
    
    
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c
    
print(f"El numero mayor es {mayor} y el menor es {menor}")