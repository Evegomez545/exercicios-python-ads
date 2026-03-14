from math import hypot
op = float(input('Qual é o comprimento do cateto oposto:'))
ad = float(input('Qual é a soma do cateto adjacente?'))
hi = hypot(op,ad)
print('A hipotenusa vai medir {:.2f}'. format(hi))


