lista = ('')

produto = ''
preco = 0.0
total = 0
fatura = []


i = 's'
while i == 's':
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço: '))
    fatura.append([produto, preco])
    total += preco
    i = input('Deseja continuar: (s ou n) :').lower()
   
for x in fatura:
    print(x[0],':',x[1])

print('Total da fatura é = ', total)

    