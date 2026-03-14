Largura = float(input('Largura da parede:'))
Altura = float(input('Altura da parede:'))
área = Largura*Altura
print('Sua parede tem a dimensão de {}x{} e sua área é {}m2'. format(Largura,Altura,área))
tinta=área/2
print('para pintar essa parede, você precisará de {}l de tinta'. format(tinta))
