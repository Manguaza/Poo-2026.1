print("Digite quatro valores inteiros")

# Lê os 4 números
numeros = []
for i in range(4):
    numero = int(input())
    numeros.append(numero)

# Calcula soma dos pares e ímpares
soma_pares = 0
soma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

# Exibe resultado
print(f"Soma dos pares = {soma_pares}")
print(f"Soma dos ímpares = {soma_impares}")



