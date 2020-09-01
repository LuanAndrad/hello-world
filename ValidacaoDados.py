lista = ('')

produto = ''
preco = 0.0
total = 0
valid_preco = False
fatura = []


i = 's'
while i == 's':
    produto = input('Digite o nome do produto: ')
    

    while valid_preco == False:
        preco = input('Digite o preço: ')
        try:
            preco = float(preco)
            if preco <= 0:
                print:('O preço precisa ser maior que 0: ')
            else:
                valid_preco = True
        except:
            print('Formato de preço inválido')

    fatura.append([produto, preco])
    total += preco
    valid_preco = False
    i = input('Deseja continuar: (s ou n) :').lower()
   
for x in fatura:
    print(x[0],':',x[1])

print('Total da fatura é = ', total)

    