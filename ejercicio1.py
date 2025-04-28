import random 
nombre = input("ingrese su nombre: ") #Pedro
tipo_cliente = input("ingrese el tipo de cliente: (Normal - Frecuente - Premium - Empresarial - Adulto Mayor) \n").capitalize() #Frecuente
#normal - NORMAL
monto = int(input("ingrese el monto de la compra: $"))
metodo_pago = input("ingrese el metodo de pago: (Efectivo - Debito - Credito) \n").capitalize() #Debito

descuento = 0
recargo = 0

nombre_minuscula = nombre.lower()

if nombre.find("a") != -1 or nombre.find("e") != -1 or nombre.find("u") != -1:
    print("tu nombre tiene descuento")
    descuento += 0.02


if tipo_cliente == "Normal" and monto >= 100000:
    descuento += 0.05
elif tipo_cliente == "Frecuente" and monto >= 80000:
    descuento += 0.1
elif tipo_cliente == "Premium" and monto >= 50000:
    descuento += 0.15
elif tipo_cliente == "Empresarial" and monto >= 200000:
    descuento += 0.2
elif tipo_cliente == "Adulto Mayor" and monto >= 30000:
    descuento += 0.08

if metodo_pago == "Efectivo" and monto >= 50000:
    descuento += 0.03
elif metodo_pago == "Credito" and monto <= 20000:
    recargo += 0.05



#rango 1 a 10
numero_aleatorio = random.randint(1, 10)

if numero_aleatorio == 7 or numero_aleatorio == 9:
    descuento += 0.05
elif numero_aleatorio == 1 or numero_aleatorio == 2:
    recargo += 0.02
elif numero_aleatorio == 5:
    print("ganaste un cupon.... que suerte (no se puede utilizar en esta compra)")
    