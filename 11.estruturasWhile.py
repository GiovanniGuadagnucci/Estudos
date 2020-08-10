# sexo = input('Digite o Sexo M/F ')
# while sexo != ('M' or 'F'):
#     sexo = input('Esse Valor não é valido, digite outro ')
# print('Beleza voce é {}'.format(sexo))

# import random
#
# n = random.randint(0,10)
# print(n)
# p = int(input('chute um numero entre 0 e 10: '))
# c = 0
# while p != n:
#     if p > n:
#         p = int(input('chute outro numero menor 0 e 10: '))
#     else:
#         p = int(input('chute outro numero maior 0 e 10: '))
#     c += 1
# print('parabens, voce finalmente acertou. Foram {} tentativas'.format(c))

# n1 = int(input('Digite um numero '))
# n2 = int(input('Digite um numero '))
# comando = 0
#
# while comando != (1,2,3,4,5):
#     comando = int(input('1 - somar \n'
#               '2 - multiplicar \n'
#               '3 - maior \n'
#               '4 - novos números \n'
#               '5 - sair do programa \n'))
#     if comando == 1:
#         print('{}'.format(n1 + n2))
#     elif comando == 2:
#         print(n1 * n2)
#     elif comando == 3:
#         print(max(n1, n2))
#     elif comando == 4:
#         n1 = int(input('Digite um numero '))
#         n2 = int(input('Digite um numero '))
#     elif comando == 5:
#         print('obrigado')
#         break
#     else:
#         print('comando invalido')
# import math
# n = int(input('Digite o numero para o fatorial: '))
# f = 1
# c = n
# while c > 0:
#     f *= c
#     c -= 1
# print(f)

# primeiro = int(input('termo '))
# razao = int(input('razao '))
# c = 0
# termo = 10
# while c <= termo:
#     print(' {}'.format(primeiro))
#     primeiro += razao
#     c += 1
# novotermo = int(input('quantos tempos voce quer a mais? '))
# s = novotermo + termo
# if novotermo == 0:
#     print('fim')
# else:
#     while c <= s :
#         print(' {}'.format(primeiro))
#         primeiro += razao
#         c += 1