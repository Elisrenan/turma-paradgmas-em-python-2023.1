numeros = str(input("digite três números, dando espaço após o outro")).split(" ")
maior = min(int(numeros[0]), int(numeros[1]), int(numeros[2]))
menor = min(int(numeros[0]), int(numeros[1]), int(numeros[2]))
print(f"O maior número é {maior} e o menor é {menor}")