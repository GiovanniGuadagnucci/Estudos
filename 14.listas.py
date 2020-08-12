import random
import collections

# lista = list()
# listapares = list()
# listaimpares = list()

# for num in range(0, 5):
#     lista.append(random.randint(0, 10))
# print(lista)
# print(f'O maior valor é {max(lista)} e está na {lista.index(max(lista))+1} posição')
# print(f'O menor valor é {min(lista)} e está na {lista.index(min(lista))+1} posição')

# while True:
#     number = random.randint(0, 10)
#     if number not in lista:
#         lista.append(number)
#     else:
#         print(f'não vou adicionar o valor {number}')
#     print(lista)
#
#     resp = input('Deseja continuar? S/N ').strip().upper()
#     if resp == 'N':
#         break
#     elif len(lista) >= 11:
#         break
# print(sorted(lista))

# while True:
#     number = random.randint(0, 10)
#     if number not in lista:
#         lista.append(number)
#     else:
#         print(f'não vou adicionar o valor {number}')
#     print(lista)
#
#     resp = input('Deseja continuar? S/N ').strip().upper()
#     if resp == 'N':
#         break
#     elif len(lista) >= 11:
#         break
# if 5 in lista:
#     print('O valor 5 está na lista')
# else:
#     print('O valor 5 não está na lista')
# print(sorted(lista,reverse=True))

# while True:
#     lista.append(random.randint(0, 10))
#
#     resp = input('Deseja continuar? S/N ').strip().upper()
#     if resp == 'N':
#         break
#     elif len(lista) >= 11:
#         break
# for number in lista:
#     if number % 2 == 0:
#         listapares.append(number)
#     else:
#         listaimpares.append(number)
# print(lista)
# print(listapares)
# print(listaimpares)

# str = str(input('Digite a expressao: '))
# teste = list()
# for digito in str:
#     if digito == '(':
#         teste.append(digito)
#     elif digito == ')':
#         if len(teste) > 0:
#             teste.pop()
#         else:
#             teste.append(digito)
#             break
# if len(teste) == 0:
#     print('valida')
# else:
#     print('invalida')
# print(teste)
# temp = []
# lista = []
# while True:
#     temp.append(str(input('Digite o nome: ')))
#     temp.append(float(input('Digite o peso: ')))
#     if len(lista) == 0:
#         maior = menor = temp[1]
#     else:
#         if temp[1] > maior:
#             maior = temp[1]
#         elif temp[1] < menor:
#             menor = temp[1]
#     lista.append(temp[:])
#     temp.clear()
#     resp = input('Deseja continuar? S/N ').strip().upper()
#     if resp == 'N':
#         break
# print(f'Deu certo {temp}')
# for valor in lista:
#     if valor[1] == maior:
#         print(f'Os mais pesados sao {valor[0]}')
#     elif valor[1] == menor:
#         print(f'Os mais leves são {valor[0]}')
# print(maior)
# print(menor)
# print(lista)

# njogos = int(input('Quanto jogos: '))
# lista = list()
# jogos = list()
# c = 0
# c2 = 1
# for jogo in range(0, njogos):
#     numeros = random.sample(range(1,60),6)
#     numeros.sort()
#     print(f'Jogo {c+1}: {numeros}')
#     c+=1

ficha = list()
while True:
    nome = str(input('Nome: '))
    if nome == 'sair':
        break
    n1 = (random.randint(0, 10))
    n2 = (random.randint(0, 10))
    media = (n2 + n2) / 2
    ficha.append([nome, [n1, n2], media])
print(ficha)
