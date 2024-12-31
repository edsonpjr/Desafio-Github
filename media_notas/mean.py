# Cálculo da média de notas

qtd_notas = int(input('Digite a quantidade de notas: '))

# Solicitando as notas do usuário
notas = [float(input(f'Digite a {i+1}ª nota: ')) for i in range(qtd_notas)]

# Calculando a média das notas
media = sum(notas) / qtd_notas
print(f'A média das notas é: {media:.2f}')

