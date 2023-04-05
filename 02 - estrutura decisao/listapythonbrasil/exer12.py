try:
  qtd_horas = input("Informe quantas horas trabalhou: ")
  if int(qtd_horas) >= 20:
    vl_hora = input("Informe o valor da hora: ")
    salario = qtd_horas * vl_hora
    if salario <= 900:
      pass
    elif salario > 900 and salario <= 1500:
      pass
    elif salario > 1500 and salario <= 2500:
      pass 
    else:
      pass
  else:
    print("Quantidade mínima exigida por esse sistema é de 20h")
except:
  print("Houve um erro!")