"""
Equipo 02 - Práctica 01
Programa por medio del cual un empleado puede consultar el monto que recibirá de comisiones por los productos que vendió mensualmente
"""

#Se establecen los valores de los 4 productos.
producto_1 = 2040
producto_2 = 5567.50
producto_3 = 850.38
producto_4 = 1000

#Se establecen variables para que el empleado pueda ingresar sus datos.
sexo = int(input("Ingrese su tipo de sexo (1 si es masculino y 2 si es femenino): "))
antigüedad = int(input("Ingrese sus años de antiguedad en la empresa (en caso de ser menor a 1 escriba 0): "))
cantidad_vendido_1 = int(input("Ingrese la cantidad de producto(s) número 1 que ha vendido durante el mes: "))
cantidad_vendido_2 = int(input("Ingrese la cantidad de producto(s) número 2 que ha vendido durante el mes: "))
cantidad_vendido_3 = int(input("Ingrese la cantidad de producto(s) número 3 que ha vendido durante el mes: "))
cantidad_vendido_4 = int(input("Ingrese la cantidad de producto(s) número 4 que ha vendido durante el mes: "))

#Se establecen variables que calculan el total vendido por el empleado de cada uno de los 4 productos.
total_producto_1 = producto_1 * cantidad_vendido_1
total_producto_2 = producto_2 * cantidad_vendido_2
total_producto_3 = producto_3 * cantidad_vendido_3
total_producto_4 = producto_4 * cantidad_vendido_4

#Dependiendo de la antigüedad del empleado se calculara el monto de la comisión que recibirá por la venta de cada producto.
if antigüedad < 1:
   print ("El monto de comision que recibirá por vender producto(s) número 1 es: $" + str(total_producto_1 * 0.13))
   print ("El monto de comision que recibirá por vender producto(s) número 2 es: $" + str(total_producto_2 * 0.02))
   print ("El monto de comision que recibirá por vender producto(s) número 3 es: $" + str(total_producto_3 * 0.185))
   print ("El monto de comision que recibirá por vender producto(s) número 4 es: $" + str(total_producto_4 * 0.04))
elif 1 <= antigüedad < 3:
   print ("El monto de comision que recibirá por vender producto(s) número 1 es: $" + str(total_producto_1 * 0.15))
   print ("El monto de comision que recibirá por vender producto(s) número 2 es: $" + str(total_producto_2 * 0.05))
   print ("El monto de comision que recibirá por vender producto(s) número 3 es: $" + str(total_producto_3 * 0.20))
   print ("El monto de comision que recibirá por vender producto(s) número 4 es: $" + str(total_producto_4 * 0.06))
elif 3 <= antigüedad < 5:
   print ("El monto de comision que recibirá por vender producto(s) número 1 es: $" + str(total_producto_1 * 0.155))
   print ("El monto de comision que recibirá por vender producto(s) número 2 es: $" + str(total_producto_2 * 0.07))
   print ("El monto de comision que recibirá por vender producto(s) número 3 es: $" + str(total_producto_3 * 0.22))
   print ("El monto de comision que recibirá por vender producto(s) número 4 es: $" + str(total_producto_4 * 0.077))
elif antigüedad >= 5 and sexo == 1:
   print ("El monto de comision que recibirá por vender producto(s) número 1 es: $" + str(total_producto_1 * 0.18))
   print ("El monto de comision que recibirá por vender producto(s) número 2 es: $" + str(total_producto_2 * 0.10))
   print ("El monto de comision que recibirá por vender producto(s) número 3 es: $" + str(total_producto_3 * 0.25))
   print ("El monto de comision que recibirá por vender producto(s) número 4 es: $" + str(total_producto_4 * 0.122))
elif antigüedad >= 5 and sexo == 2:
   print ("El monto de comision que recibirá por vender producto(s) número 1 es: $" + str(total_producto_1 * 0.20))
   print ("El monto de comision que recibirá por vender producto(s) número 2 es: $" + str(total_producto_2 * 0.12))
   print ("El monto de comision que recibirá por vender producto(s) número 3 es: $" + str(total_producto_3 * 0.27))
   print ("El monto de comision que recibirá por vender producto(s) número 4 es: $" + str(total_producto_4 * 0.142))


print ("FIN DEL PROGRAMA")
