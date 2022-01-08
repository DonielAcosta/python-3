menu ="""
Bienvenidos al conversor de Monedas

1 -Pesos Colombianos
2 -Pesos Argentinos
3 -Pesos Mexicanos
4 -Bolivares


ELige una opcion: """

def conversor(tipo_moneda, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_moneda +"tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "Dolares")
opcion = int(input(menu))

if opcion == 1:
  conversor("Colombianos,3875")
elif opcion == 2:
    conversor("Argentina,65")
elif opcion == 3:
    conversor("Mexicanos,24")
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



