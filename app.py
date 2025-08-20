# Inicializa as variáveis
soma = 0
quantidade = 0

# Lê o primeiro número antes de iniciar o loop
print("Digite números inteiros. Digite 0 para finalizar.")
numero = int(input("Digite um número: "))

# O loop continua enquanto o número digitado for diferente de 0
while numero != 0:
    soma += numero
    quantidade += 1
    # Lê o próximo número dentro do loop
    numero = int(input("Digite outro número: "))

# Calcula e exibe os resultados
if quantidade > 0:
    media = soma / quantidade
    print(f"\nResultados:")
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma dos números: {soma}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhum número foi digitado (além do 0 para sair).")