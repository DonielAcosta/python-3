# cont = 0
# print('2 elevado a ' + str(cont) + 'es igual a:' + str(2**cont))

def run():
   LIMITE = 1000

   cont = 0
   potencia_2 = 2**cont
   while potencia_2 < LIMITE:
       print('2 elevado a ' + str(cont) + ' es igual a: ' + str(potencia_2))
       cont = cont + 1
       potencia_2 = 2**cont

if __name__ == "__main__":
    run()