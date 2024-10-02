notas = []

for i in range(3):
    nota = float(input('Nota: '))
    if 0 <= nota <= 10:
        notas.append(nota)
    
if notas:
    media = sum(set(notas))/len(set(notas))
    maior_nota = max(set(notas))    
    menor_nota = min(set(notas))
    diferença = maior_nota - menor_nota

print(f'Média = {media:.2f}')
print(f'Maior nota = {maior_nota}')
print(f'Menor nota = {menor_nota}')
print(f'Diferença entre a maior e a menor nota = {diferença}')

else:
    print('Valores inválidos')
