from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento:'))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'. format (ano,idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'. format (saldo))
    print('Seu alistamento foi em {}'. format(saldo))

elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos'. format (saldo))



