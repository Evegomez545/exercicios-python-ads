import math
ângulo = float (input(' Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo do de {} tem o COSSENO  de {:.2f}'. format(ângulo, cosseno))
tângente = math.tan (math.radians (ângulo))
print('O ângulo de {} tema TÂNGENTE de {:.2f}'. format(ângulo, tângente))
