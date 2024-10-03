notas = []
for i in range(3):
    if nota >= 0 and nota <= 10:
        notas.append(float(input(f'{i+1}º nota: ')))

def media(notas):
    media = sum(set(notas))/len(set(notas))
    return media

print(f'Média = {media(notas.copy()):.2f}')
print(f'Maior nota = {max(set(notas))}')
print(f'Menor nota = {min(set(notas))}')
print(f'Diferença entre a maior e a menor nota = {max(set(notas)) - min(set(notas))}')
