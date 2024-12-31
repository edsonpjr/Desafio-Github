#Checar a paridade de um número

numero = int(input("Digite um número inteiro: "))
if numero >= 0:
    answer = "Par" if numero % 2 == 0 else "Ímpar"
    print(f"O número {numero} é {answer}.")
else:
    print("Entrada inválida.")