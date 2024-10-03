atleta = input('Atleta: ').title()

saltos = []
for i in range(5):
    saltos.append(float(input(f'{i+1}º salto: ')))

print()
ordem = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
for i in range(len(saltos)):
    print(f'{ordem[i]} salto: {saltos[i]} m')

def media(saltos):
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    media = sum(saltos)/len(saltos)
    return media

print()   
print(f'Melhor salto: {max(saltos)} m')
print(f'Pior salto: {min(saltos)} m')
print(f'Média dos demais saltos: {media(saltos.copy()):.1f} m')

print()
print(f'Resultado final:')
print(f'{atleta} - {media(saltos.copy()):.1f} m')
