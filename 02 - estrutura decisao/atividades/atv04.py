"""Comentários com mais de uma linha"""
#comentário com apenas uma linha
try:
  operacao = int(input("Escolha a operação: \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n opção:"))
  if 1 <= operacao <= 4:
    try:
      numero1 = int(input("Digite o primeiro número: "))
      numero2 = int(input("Digite o segundo número: "))
      if operacao == 1:
        soma = numero1 + numero2
        print(f"O valor da soma foi {soma}")
      elif operacao == 2:
        sub = numero1 - numero2
        print(f"O valor da subtração foi {sub}")
      elif operacao == 3:
        mult = 0
        if numero1 != 0 and numero2 != 0:
          mult = numero1 * numero2
        print(f"O valor da multiplicação foi {mult}")
      else:
        div = 0
        if numero1 != 0 and numero2 != 0:
          #usando a função round para arredondar as divisões
          div = round(numero1 / numero2)
        print(f"O valor da divisão foi {div:.2f}")
    except:
      print("Número inválido! Tente novamente misera!")
  else:
    print("Opção inválida!")
except:
  print("Erro de digitação, tente novamente!")