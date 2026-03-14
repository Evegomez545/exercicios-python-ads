peso = float(input('Qual é o seu peso?'))
altura = float(input('Qual é a sua altura?'))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é {} \nCUIDADO! Você está abaixo do peso'.format(imc))

elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f} \nPARABÉNS! Você está no peso ideal'. format(imc))

elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.1f} \n CUIDADO! Você está com sobrepeso'.format(imc))

elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f} \n CUIDADO! Você está com obesidade'.format(imc))

else:
    print('Seu IMC é {:.1f} \n CUIDADO! Você está com O'
          'SIDADE MÓRBIDA'.format(imc))