"Programa que resuelve una ecuación cuadratica de la forma ax^2 + bx + c = 0"

print("Teniendo una ecuación ax^2 + bx + c = 0")
a = int(input("Introduce el valor de a:"))
b = int(input("Introduce el valor de b:"))
c = int(input("Introduce el valor de c:"))

#Calcular las raices con los valores proporcionados
if a!=0:
    x_1 = (-b+(((b**2)-(4*a*c))**0.5))/(2*a)
    x_2 = (-b-(((b**2)-(4*a*c))**0.5))/(2*a)

    print("El vaor de x_1 es:")
    print(x_1)

    print("El vaor de x_2 es:")
    print(x_2)
    
else:
    print("Valor no válido")
