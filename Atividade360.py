n1 = float(input('Valor da casa: R$'))
n2 = float(input('Salário do comprador: R$'))
n3 = int(input('Quantidade de anos:'))
mensal = n1 / (n3*12)
limite = (n2 * 30/100)

if mensal <= limite:
    print('Para pegar uma casa de {} em {} anos de prestação de {:.2f}.'.format(n1, n3, mensal))
    print('Empréstimo APROVADO!')

else:
    print('Para pegar uma casa de {} em {} anos de prestação de {}' . format(n1,n3,mensal))
    print('Empréstimo NEGADO')
