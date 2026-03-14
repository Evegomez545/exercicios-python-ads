frase=str(input('Digite o seu nome:')).strip()
print('Analisando seu nome..')
print(frase)
print('Seu nome em Maiusculo é {}'. format(frase.upper()))
print('Seu nome em Minusculo é {}'. format(frase.lower()))
print('O nome completo tem {} letras'.format(len(frase) - frase.count(' ')))
print('Seu primeiro nome tem {} letras'.format(frase.find(' ')))





