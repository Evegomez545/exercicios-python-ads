from random import randint
distancia = randint(0,200)
viagem = float(input("Qual é a distância da viagem: "))

if distancia <= 200:
    preço = viagem * 0.50
    print('Você está preste a começar uma viagem de {}Km'.format(viagem))
    print('E o preço da sua passagem será de R$ {}'.format(viagem * 0.50))

else:
    preço = viagem * 0.45
    print('Você está preste a começar uma viagem de {}Km'.format(viagem))
    print('E o preço da sua passagem será de R$ {}'.format(viagem * 0.45))





