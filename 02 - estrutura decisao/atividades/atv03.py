try:
  numero = int(input("Informe um número entre 0 e 1000: "))
  if 0 < numero < 10000:
    if numero % 4 == 0:
      print("O número é divisível por 4")
    else:
      print("O número não é divisível por 4")
  else:
    print("Número fora do range, tente novamente!")
except:
  print("Número inválido!")