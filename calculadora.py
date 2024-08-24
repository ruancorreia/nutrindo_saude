# ENTRADA DE DADOS
nome = input('Digite o nome do paciente: ')
idade = int(input('Digite a idade do paciente: '))
sexo = int(input('Digite o sexo do paciente. 1 para masculino, 0 para feminino: '))
peso = int(input('Digite o peso registrado: '))
altura = float(input('Digite a altura do paciente: '))
cintura = float(input('Digite a circunferencia da cintura: '))
imc = peso / (altura * altura)

metodo_medicao = int(input('Qual método está utilizando para medição? (1) Adipômetro || (2) Bioimpendâcia: '))
# ADIPOMETRO
if(metodo_medicao == 1):
  if(sexo ==  1):
    peito = float(input('Digite a medida da dobra cutânea do peito em mm:'))
    abdomen = float(input('Digite a medida da dobra cutânea do abdomen em mm:'))
    coxa = float(input('Digite a medida da dobra cutânea da coxa em mm:'))
    soma_dobra = peito + abdomen + coxa
    densidade_corporal = 1.10938 - (0.0008267 * soma_dobra) + (0.0000016 * soma_dobra ** 2) - (0.0002574 * idade)
    porcentagem_gordura = (4.95 / densidade_corporal - 4.50) * 100
  elif(sexo == 0):
    triceps = float(input('Digite a medida da dobra cutânea do tríceps em mm: '))
    supra_iliaca = float(input('Digite a medida da dobra cutânea da supra iliaca em mm:'))
    coxa = float(input('Digite a medida da dobra cutânea da coxa em mm:'))
    soma_dobra = triceps + supra_iliaca + coxa
    densidade_corporal = 1.0994921 - (0.0009929 * soma_dobra) + (0.0000023 * soma_dobra ** 2) - (0.0001392 * idade)
    porcentagem_gordura = (4.95 / densidade_corporal - 4.50) * 100
  else:
    print('Valores incorretos! Digite novamente.')
# BIOIMPEDANCIA
elif(metodo_medicao == 2):
  if(sexo ==  1 ):
    porcentagem_gordura = 1.2 * imc + 0.23 * idade - 10.8 * sexo - 5.4
    print(f'O percentual de gordura corporal é: {porcentagem_gordura:.2f}')
  elif(sexo == 2):
    porcentagem_gordura = 1.2 * imc + 0.23 * idade - 10.8 * sexo - 5.4
    print(f'O percentual de gordura corporal é: {porcentagem_gordura:.2f}')
  else:
    print('Valores incorretos! Digite novamente.')

# IMC ADULTOS / IDOSOS
  if idade <=59:
    if imc <= 18.49:
      print('Abaixo do Peso!')
    elif imc >= 18.5 and imc <= 24.99:
      print('Imc Adequado!')
    elif imc >= 25 and 29.99:
      print('Sobrepeso!')
    elif imc >= 30 and imc <= 34.99:
      print('Obesidade grau I')
    elif imc >= 35 and imc <= 39.99:
      print('Obesidade Grau II')
    else:
      print('Obesidade Grau III')
  else:
    if imc <= 22:
      print('Baixo Peso')
    elif imc >= 22.01 and imc >= 26.99:
      print('Adequado!')
    else:
      print('Sobrepeso!')
  
# Circunferencia da cintura
if sexo == 0:
  if cintura <= 79:
    print('Circunferencia da cintura adequada')
  else:
    print('Circunferencia da cintura elevada!')
elif sexo == 1:
  if cintura <= 93:
    print('Circunferencia da cintura adequada!')
  else:
    print('Circunferencia da cintura elevada!')
else:
  print('Dados Inválidos!')

# Porcentagem de gordura corporal
if sexo == 0:
  if idade >= 20 and idade <= 39:
    if porcentagem_gordura <= 21:
      print('Porcentagem de gordura baixa!')
    elif porcentagem_gordura >= 21.1 and porcentagem_gordura <= 32.9:
      print('porcentagem de gordura adequada!')
    else:
      print('Porcentagem de gordura alta!')
  elif idade >= 40 and idade <= 59:
    if porcentagem_gordura <= 23:
      print('Porcentagem de gordura baixo!')
    elif porcentagem_gordura <= 23.1 and porcentagem_gordura >= 33.9:
      print('Porcentagem de gordura adequada!')
    else:
      print('Porcentagem de gordura Alta!')
  elif idade >= 60 and idade <= 79:
      if porcentagem_gordura <= 24:
        print('Porcentagem de gordura baixa!')
      elif porcentagem_gordura >= 24.1 and porcentagem_gordura <= 35.9:
        print('Porcentagem de gordura adequada!')
      else:
        print('Porcentagem de gordura alta!')
elif sexo == 1:
  if idade >= 20 and idade <= 39:
    if porcentagem_gordura <= 8:
      print('porcentagem de gordura baixa')
    elif porcentagem_gordura >= 8.1 and porcentagem_gordura <= 19.9:
      print('Porcentagem de gordura adequada!')
    else:
      print('Porcentagem de gordura alta!')
  elif idade >= 40 and idade <= 59:
      if porcentagem_gordura <= 11.0:
        print('Porcentagem de gordura baixa!')
      elif porcentagem_gordura >= 11.1 and porcentagem_gordura <= 21.9:
        print('Porcentagem de gordura adequada')
      else:
        print('Porcentagem de gordura alta')
  elif idade >= 60 and idade <= 79:
      if porcentagem_gordura <= 13:
        print('Porcentagem de gordura baixa!')
      elif porcentagem_gordura <= 13.1 and porcentagem_gordura <= 24.9:
        print('Porcentagem de gordura adequada')
      elif porcentagem_gordura > 25:
        print('Porcentagem de gordura alta!')
      else:
        print('Dados inválidos ou nao conclusivos! por gentileza verifique os valores informados e tente novamente!')
  else:
    print('Dados inválidos ou nao conclusivos! por gentileza verifique os valores informados e tente novamente!')


