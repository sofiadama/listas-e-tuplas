numeros = (17, 28, 94, 57, 13, 16, 68, 2, 37, 49)

maior_numero = max(numeros)
menor_numero = min(numeros)

posiçao_maior = numeros.index(maior_numero)
posiçao_menor = numeros.index(menor_numero)

print(f'O maior elemento é {maior_numero} e ocupa a {posiçao_maior + 1}º posição.')
print(f'O menor elemento é {menor_numero} e ocupa a {posiçao_menor + 1}º posição.')