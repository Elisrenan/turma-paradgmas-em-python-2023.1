num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))
num3 = int(input("Digite o primeiro número: "))

if num1 > num2 and num1 > num3:
  print(f"O maior número é o número {num1}")
elif num2 > num1 and num2 > num3:
  print(f"O maior número é o número {num2}")
else:
  print(f"O maior número é o número {num3}")