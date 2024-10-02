N = int(input('Elementos: '))
K = int(input('K: '))

X = []
for i in range(N):
    num = int(input())
    X.append(num)

for y in X:
    produto = y*K
    print(produto, end=' ')
