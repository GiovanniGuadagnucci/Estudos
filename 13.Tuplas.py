# lanche = ('hamburguer', 'suco', 'Pizza', 'Pudim')
# print(lanche)
# print(lanche[1])
# print(lanche[0:2])
# print(lanche[-1])
# print(lanche[:2])
# print(lanche[-2:])
#
# for c in lanche:
#     print(c, end=' ')
# print('-'*20)
#
# c = 0
# while c < len(lanche):
#     print(lanche[c], end=' ')
#     c += 1

# t = ('um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
# n = int(input('Digite um numero de 0 a 10: '))
# while n > 10 or n < 0:
#     n = int(input('numero inválido digite de 0 a 10: '))
# ext = t[n-1]
# print(f'O numero por extenso é {ext}')

# brasileirao = ('Athletico-PR','Sport', 'Recife','Atlético-MG'
#                ,'Grêmio','Internacional','Bragantino','Santos'
#                ,'Atlético-GO','Bahia','Botafogo','Corinthians'
#                ,'Goiás','Palmeiras','São Paulo','Vasco da Gama'
#                ,'Ceará','Coritiba','Flamengo','Fluminense','Fortaleza')
# print(f'Os primeiros 5 times são {brasileirao[:5]}')
# print(f'Os ultimos 4 colocados são {brasileirao[-4:]}')
# pos = brasileirao.index('Sport') + 1
# print(f'Times ordem alfabetica {sorted(brasileirao)}')
# print(f'o Sport está na {pos} posição')

# import random
#
# tupla = (random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)
#          ,random.randint(0, 10),random.randint(0, 10))
# print(tupla)
# print(max(tupla))
# print(min(tupla))


# tupla = ('aprender', 'programar')
# vogais = 'aeiou'
# resp = ''
# for palavra in tupla:
#     print('-'*20)
#     for char in palavra:
#         if char in vogais:
#             resp += (char + ' ')
#     print(f'Na palavra {palavra} temos {resp}')



