
print ('************************************************************')
print ('*** PROGRAMA QUE INVERTE A FRASE DIGITADA ******************')
print ('*****************  RAFAEL MESQUITA *************************')
print ('****** SISTEMAS DE INFORMAÇÃO - UNIS - POO PYTHON **********')
print ('************************************************************')

print ('')
frase = input('Digite uma frase: ')
print(' Você digitou: {}'.format(frase))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('')
print('A frase que você digitou invertida fica: {}'.format(invertida))
