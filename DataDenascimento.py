meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro" ,"Dezembro")
data_nascimento = input('Digite sua data de nascimento no formato DD/MM/AAAA: ')
mes = int(data_nascimento[3:5])
print('Você nasceu no mês:',meses[mes-1])