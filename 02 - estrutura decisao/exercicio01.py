numero = float(input("Informe um número: "))
numero2 = float(input("Informe o segundo número: "))
if numero > numero2:
  print(f"O primeiro número: {numero} é o maior")
elif numero < numero2:
  print(f"O segundo número: {numero2} é o maior")
else:
  print("Resultado inválido!")