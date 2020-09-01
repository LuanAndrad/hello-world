valid_sexo = False
sexo = input('Digite seu sexo F ou M: ').lower()
while valid_sexo == False:
    #sexo1 = input('Digite seu sexo F ou M: ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F')
    else:
       valid_sexo = True
   


peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

def calcula_imc(peso,altura):
    valor = peso / (altura**2)
    return(valor)
#####
valor = calcula_imc(peso,altura)

if sexo == 'f':
    if valor < 19.1:
        print('Abaixo do peso')
    elif valor >= 19.1 and valor < 25.8:
        print('No peso normal')
    elif valor >= 25.8 and valor < 27.3:
        print('Marginalmente acima do peso')
    elif valor >= 27.3 and valor < 32.3:
        print('Acima do peso ideal')  
    else:
        print('Obeso')

if sexo == 'm':
    if valor < 20.7:
        print('Abaixo do peso')
    elif valor >= 20.7 and valor < 26.4:
        print('No peso normal')
    elif valor >= 26.4 and valor < 27.8:
        print('Marginalmente acima do peso')
    elif valor >= 27.8 and valor < 31.1:
        print('Acima do peso ideal')  
    else:
        print('Obeso')



