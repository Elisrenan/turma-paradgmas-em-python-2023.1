try:
  idade = int(input("Informe sua idade: "))
  if idade >= 16:
    print("Pode votar")
  else:
    print("Não pode votar!")
except:
  print("Número inválido, tente novamente!")