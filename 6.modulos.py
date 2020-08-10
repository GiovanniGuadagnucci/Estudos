import math
import random

n = random.uniform(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(0, 360)
alunos = ['joao', 'maria', 'pedro', 'joaquim']
random.shuffle(alunos)

print('{:.2f}'.format(n))
print('{:.2f}'.format(n2))
print('{:.2f}'.format(n3))
print('sua parte interia é {}'.format(math.trunc(n)))
print('A hipotenuza é {:.2f}'.format(math.hypot(n, n2)))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(math.radians(n3)), math.cos(math.radians(n3)), math.tan(math.radians(n3))))
print('O aluno que foi sorteado foi {}'.format(random.choice(alunos)))
print('A ordem sorteada foi {}'.format(alunos))
