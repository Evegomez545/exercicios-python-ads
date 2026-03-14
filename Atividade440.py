preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista em dinheiro / cheque
[ 2 ] á vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra foi parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas?'))
    parcela = total / totalparc
    print('Sua comprfa será parcelada em {}x de R$ {:.2f} COM JUROS'. format(totalparc, parcela))
else:
    total = 0
    print('opção invalida de pagamento, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,total))





