n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
n = (n1 + n2) / 2
d1 = 'a media é {}'.format(n)
d2 = 'o valor antecessor é {} e o sucessor é {}'.format((n - 1), (n + 1))
d3 = 'o dobro é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format((n * 2), (n * 3), (n ** (1 / 2)))
d4 = 'o valor em centimetros é {} e o valor em milimetros é {}'.format((n * 100), (n * 1000))
d5 = 'voce pode comprar {:.2f} dolares'.format(n/3,27)
d6 = 'Os metros quadrados são {} e a quantidade de litros de tinta é {}'.format((n1*n2), ((n1*n2)/2))
d7 = 'O valor final do desconto desse produto é {}'.format(n*0.95)
d8 = 'O seu novo salário é {}'.format(n*1.15)

print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print(d8)

for valor in range(11):
    print('{} x {} = {}'.format((n), (valor), (n * valor)))

