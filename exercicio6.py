atleta = input('Atleta: ')

saltos = []
texto = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
for i in range(5):
    salto = float(input())
    saltos.append(salto)
    print(f'{texto[i]} salto: {saltos[i]} m')

def media(saltos):
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    media = sum(saltos)/len(saltos)
    return media

print(f'Melhor salto: {max(saltos)} m')
print(f'Pior salto: {min(saltos)} m')
print(f'Média dos demais saltos: {media(saltos.copy()):.1f} m')
print()
print(f'Resultado final:')
print(f'{atleta}: {media_saltos:.1f} m')