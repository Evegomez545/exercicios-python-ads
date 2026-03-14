salario = float(input('Qual é o salário do funcionário:'))
if salario <= 1250:
    novo = salario + (salario * 15 /100)
else:
    novo = salario + (salario *10 / 100)
print('Quem ganhava R${} passa a ganhar R${} agora'.format(salario,novo))



