nome = input('digite seu nome ').strip().lower()
nometratado = nome.replace(' ', '')
primeironome = nome.split()
print(nome.upper())
print(nome.lower())
print(len(nometratado))
print(len(primeironome[0]))
print('a letra a aparece {}'.format(nometratado.count('a')))
print('a primeira vez aparece na posição {}'.format(nometratado.find('a')))
print('a ultima vez aparece na posição {}'.format(nometratado.rfind('a')))
print('Seu primeiro nome é {}'.format(primeironome[0]))
print('Seu ultimo nome é {}'.format(primeironome[-1]))

n = input('Digite um numero ')
nlist = list(n)
print('O milhar é {}'.format(nlist[0]))
print('O centena é {}'.format(nlist[1]))
print('O dezena é {}'.format(nlist[2]))
print('O unidade é {}'.format(nlist[3]))

cidade = input('Qual cidade voce nasceu? ').strip().lower().split()
print('santo' in cidade)
print(cidade[0] == 'santo')