# s = 0
# c = 0
# while True:
#     n = int(input('Digite um numero: '))
#     if n == 999:
#         break
#     c += 1
#     s += n
# print(f'Foram {c} ditados e a soma foi {s}')

# c = 0
# while True:
#     tab = int(input('Digite o numero que quiser '))
#     if tab < 0:
#         break
#     for c in range(0, 11):
#         print('-'*10)
#         print(f'{c} x {tab} = {c * tab}')
#         c+=1
# print('Fim')

# import random
# contador = 0
# npc = random.randint(0, 10)
# while True:
#     escolha = input('Par ou Impar? ').strip().lower()
#     if escolha == 'par':
#         jogador = int(input('Qual numero? '))
#         soma = jogador + npc
#         if soma % 2 == 0:
#             print(f'{soma} é par, Voce ganhou parabens, vamos outra vez')
#             contador += 1
#             print(contador)
#         else:
#             print(f'{soma} é impar Voce perdeu')
#             break
#     elif escolha == 'impar':
#         jogador = int(input('Qual numero? '))
#         soma = jogador + npc
#         if soma % 2 != 0:
#             print(f'{soma} é impar, Voce ganhou parabens, vamos outra vez')
#             contador += 1
#             print(contador)
#         else:
#             print(f'{soma} é par Voce perdeu')
#             break
#     else:
#         print('escolha não valida. Digite par ou impar')
# print(f'Voce ganhou {contador}. Fim')
# tot18 = toth = totf = 0
# while True:
#     idade = int(input('Qual a idade da pessoa? '))
#     sexo = ' '
#     while sexo not in 'mf':
#         sexo = str(input('Sexo M/F ')).strip().lower()[0]
#     if idade >=18:
#         tot18 +=1
#     if sexo == 'm':
#         toth += 1
#     if sexo == 'f' and idade < 20:
#         totf += 1
#
#     escolha = ' '
#     while escolha not in 'sn':
#         escolha = str(input('Quer Continuar? S/N ')).strip().lower()[0]
#     if escolha == 'n':
#         break
#
# print(f'{tot18} +18')
# print(f'{toth} homens')
# print(f'{totf} mulher < 20')

totpreco = totmil = menor = cont =0
prod = ''

# while True:
#     nome = str(input('Nome do Produto: '))
#     preco = float(input('Preço: '))
#     cont +=1
#     totpreco += preco
#     if preco > 1000:
#         totmil +=1
#     if cont == 1:
#         menor = preco
#     else:
#         if preco < menor:
#             prod = nome
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar S/N: ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'o total foi {totpreco}')
# print(f'o total de mais de 1000 foi {totmil}')
# print(f'o produto mais barato é {prod} e custa {menor}')