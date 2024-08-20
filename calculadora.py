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






