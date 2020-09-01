def mensagem(nome):
    print('Seja bem vindo ' + nome.title())

user = 'Luan'

mensagem(user)

def imc(peso, altura):
    valor = peso / (altura**2)
    return(valor)

if imc(72, 1.80) > 20:
    print('ta top')