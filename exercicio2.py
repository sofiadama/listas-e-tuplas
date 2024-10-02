elementos = int(input('Quantidade de elementos: '))

inteiros = []
for i in range(elementos):
    numero = int(input())
    inteiros.append(numero)

if len(inteiros) != len(set(inteiros)):
    repetidos = inteiros.count(numero)
# set() não permite elementos duplicados
    print(f'Há {repetidos} números repetidos.')
else:
    print('Não há números repetidos.')
