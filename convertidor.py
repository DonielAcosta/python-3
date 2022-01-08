menu ="""
Bienvenidos al conversor de Monedas

1 -Pesos Colombianos
2 -Pesos Argentinos
3 -Pesos Mexicanos
4 -Bolivares


ELige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "Dolares")

elif opcion == 2:
    pesos = input("¿Cuantos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "Dolares")

elif opcion == 3:
    pesos = input("¿Cuantos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "Dolares")

elif opcion == 4:
    bolivares = input("¿Cuantos Bolivares tienes?: ")
    bolivares = float(bolivares)
    valor_dolar = 4.90
    dolares = bolivares/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "Dolares")

else:
    print('Ingresa una opcion correcta  porfavor ')



