
print ('************************************************************')
print ('*** PROGRAMA QUE INFORMA SE O NUMERO E PRIMO ***************')
print ('*****************  RAFAEL MESQUITA *************************')
print ('****** SISTEMAS DE INFORMAÇÃO - UNIS - POO PYTHON **********')
print ('************************************************************')

print ('')
print ('')

num = int(input("Digite um número: "))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

print("O número {} foi divisível {} vezes!".format(num, contador))

if contador == 2:
    print ('')
    print("O número é primo")
else:
    print ('')
    print("O número não é primo")
