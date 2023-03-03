"""
Equipo 02 - Práctica 01
Programa por medio del cual un empleado puede consultar el monto que recibirá de comisiones por los productos que vendió mensualmente
"""

#Se establecen los valores de los 4 productos
producto_1 = 2040
producto_2 = 5567.50
producto_3 = 850.38
producto_4 = 1000

#Se establecen variables para que el empleado pueda ingresar sus datos
sexo = input("Ingrese su tipo de sexo (M si es masculino, F si es femenino): ")
antigüedad = int(input("Ingrese sus años de antiguedad en la empresa: "))
producto_vendido_1 = int(input("Ingrese la cantidad de producto(s) número 1 que ha vendido durante el mes: "))
producto_vendido_2 = int(input("Ingrese la cantidad de producto(s) número 2 que ha vendido durante el mes: "))
producto_vendido_3 = int(input("Ingrese la cantidad de producto(s) número 3 que ha vendido durante el mes: "))
producto_vendido_4 = int(input("Ingrese la cantidad de producto(s) número 4 que ha vendido durante el mes: "))

if antigüedad < 1:
 print (producto_1 *0.13)
 print (producto_2 *0.02)
 print (producto_3 *0.185)
 print (producto_4 *0.04)
