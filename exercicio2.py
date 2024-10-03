n = int(input('Quantidade de elementos: '))

inteiros = []
for i in range(n):
    inteiros.append(int(input(f'{i+1}º número: ')))

if len(inteiros) != len(set(inteiros)):
    repetidos = inteiros.count(numero)
# set() não permite elementos duplicados
    print(f'Há {repetidos} números repetidos.')
else:
    print('Não há números repetidos.')
