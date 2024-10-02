def media(saltos):
    saltos.remove(melhor)
    saltos.remove(pior)
    media = sum(saltos)/len(saltos)
    return media

atleta = input('Atleta: ')

saltos = []
for i in range(5):
    salto = float(input())
    saltos.append(salto)

melhor = max(saltos)
pior = min(saltos)

print(f'Primeiro salto: {saltos[0]:.1f} m')
print(f'Segundo salto: {saltos[1]:.1f} m')
print(f'Terceiro salto: {saltos[2]:.1f} m')
print(f'Quarto salto: {saltos[3]:.1f} m')
print(f'Quinto salto: {saltos[4]:.1f} m')
print()
print(f'Melhor salto: {melhor:.1f} m')
print(f'Pior salto: {pior:.1f} m')

media_saltos = media(saltos.copy())
print(f'Média dos demais saltos: {media_saltos:.1f} m')
print()
print(f'Resultado final:')
print(f'{atleta}: {media_saltos:.1f} m')