import datetime

#Entrada de valores

print ('************************************************************')
print ('*************** LEIA IDADE *********************************')
print ('*****************  RAFAEL MESQUITA *************************')
print ('****** SISTEMAS DE INFORMAÇÃO - UNIS - POO PYTHON **********')
print ('************************************************************')


nome = input ("Como se chama? ")
ano = eval (input ("Nasceu em que ano? "))
mes = eval (input ("Nasceu em que mês? (ex: 1 "))
dia = eval (input ("Nasceu em que dia ? "))
ano_atual = eval (input ("Ano atual? "))
mes_atual = eval (input ("Mês atual? (ex: 1)"))
dia_atual = eval (input ("Dia atual? "))
dataNasc = datetime.date(ano, mes, dia)
dataAtual = datetime.date(ano_atual, mes_atual, dia_atual)

#diferença retorna em timedelta
diferenca = (dataAtual - dataNasc)
#Cálculos e Resultados
resultado = (diferenca.days / 365.25)
#ano_atual-ano

if (dia == dia_atual and mes == mes_atual):
    print ("O %s tem %d anos!" %(nome, resultado))
else:
    ((dia > dia_atual and mes == mes_atual) or mes < mes_atual)
    print ("O %s tem %d anos!" %(nome, resultado))
