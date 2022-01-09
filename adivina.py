import random



def run():
    num_ale = random.randint(1,100)
    num_elegido = int(input('Elige un numero del 1 al 100: '))
    while num_elegido != num_ale:
        if num_elegido < num_ale:
            print('Busca un numero mas grande')
        else:
            print('Busca un numero mas pequeño')
        num_elegido = int(input('Elige otro Numero: '))
    print('¡GANASTE!')

if __name__ == '__main__':
    run()