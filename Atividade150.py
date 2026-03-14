dias = int(input('Quantos dias alugados?'))
km = float (input('Quantos km rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O valor total a pagar é de: R${}'.format(pago))
