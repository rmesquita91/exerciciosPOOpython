"""
Faça um Programa que leia três números e mostre o maior e o menor deles.

"
print ('************************************************************')
print ('***  INFORMA O MAIOR E MENOR NUMERO ************************')
print ('*****************  RAFAEL MESQUITA *************************')
print ('****** SISTEMAS DE INFORMAÇÃO - UNIS - POO PYTHON **********')
print ('************************************************************')
print ('')
print ('Entre com os numeros')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
menor = n1

if maior < n2:
	maior = n2

if maior < n3: 
	maior = n3

if menor > n2:
	menor = n2

if menor > n3:
	menor = n3
	
print ('*********************************************************************') 
print ('O maior número foi:  %d ' %maior)
print ('O menor número foi:  %d ' %menor)
print ('*********************************************************************')
