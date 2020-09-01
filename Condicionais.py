'''idade = int(input('Digite a sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower()

if idade < 18 and sexo == 'm':
    print ('Homem menor de idade')
elif idade < 18 and sexo == 'f':
    print ('Mulher menor de idade')
elif idade >= 18 and sexo == 'm':
    print ('Homem maior de idade')
elif idade >= 18 and sexo == 'f':
    print ('Mulher maior de idade')'''
valid = False
try:

    Nome = input('Digite o nome do Aluno: ')
    while valid == False:

        Nota1 = float(input('Digite a nota da prova 1: '))
        Nota2 = float(input('Digite a nota da prova 2: '))
        Faltas = int(input('Digite o total de faltas: '))

        if (Nota1 or Nota2) > 10 or (Nota1 or Nota2) < 0:
            print('As notas precisam estar entre 0 e 10')
        elif Faltas > 20 or Faltas < 0:
            print('As faltas precisam estar entre 0 e 20')
        else:
            valid = True

        

    Media = (Nota1+Nota2)/2
    Total_Faltas = ((20-Faltas) / 20)*100
    Resultado = ''

    if Total_Faltas >= 70.0:
        if Media >= 6.0:
            Resultado = 'Aprovado'
        else:
            Resultado = 'Reprovado por media'
    elif Media >= 6.0:
            Resultado = 'Reprovado por falta'
    else:
            Resultado = 'Reprovado por falta e media'

    print(Nome)
    print(Media)
    print(Total_Faltas)
    print(Resultado)
except:
    print('ERRO!')


