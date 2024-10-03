N = int(input('Elementos: '))
K = int(input('K: '))

X = []
for i in range(N):
    X.append(int(input(f'{i+1}º número: ')))
    
print()
for Y in X:
    print(f'Produto de {Y} por {K}: {Y*K}')
