salário = float(input('Qual é o salário do funcionário?'))
novo = salário + (salário * 15 / 100)
print('O funcionário recebia o salário de R${:.2f}, e com 15% de aumento passa a receber R${}'.format(salário,novo))
