try:
  idade = int(input("Informe sua idade: "))
  genero = str(input("Informe M para \nmasculino e F para feminino: ")).upper()
  if idade > 0:
    if genero == "M" or genero == "F":
      if (genero == "M" and idade >= 65) or (genero == "F" and idade >= 60):
        print("Pode se aposentar")
      else:
        print("Ainda um gênero válido!")
  else:
    print("Informe uma idade válida!")
except:
  print("Idade inválida, tente novamente!")