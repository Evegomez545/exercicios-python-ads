n1=float(input('Primeira nota do aluno:'))
n2=float(input('Segunda nota do aluno:'))
media = (n1+n2)/2
if media >= 7.0:
    print('Tirando {} e {}, a média do aluno é {}'. format(n1, n2, media))
    print('O aluno está APROVADO!')

elif media >= 5.0:
    print('Tirando {} e {}, a média do aluno é {}'. format(n1, n2, media))
    print('O aluno está de RECUPERAÇÃO!')

else:
    print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, media))
    print('O aluno está REPROVADO')





