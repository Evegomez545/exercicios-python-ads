a = float(input('Digite um número:'))
b = float(input('Digite outro número:'))
c = float(input('Digite mais um número:'))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima podem formar um triangulo',end=' ')
    if a ==  b == c:
        print('EQUILATERO!')

    elif a != b != c != a:
        print('ESCALENO')

    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima não podem formar um triangulo')


