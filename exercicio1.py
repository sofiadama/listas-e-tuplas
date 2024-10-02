notas = []

for i in range(3):
    nota = float(input('Nota: '))
    if 0 <= nota <= 10:
        notas.append(nota)

def media(notas):
    media = sum(set(notas))/len(set(notas))
    return media

print(f'Média = {media(notas.copy()):.2f}')
print(f'Maior nota = {max(set(notas))}')
print(f'Menor nota = {min(set(notas))}')
print(f'Diferença entre a maior e a menor nota = {max(set(notas)) - min(set(notas))}')
