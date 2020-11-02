import sys

print ('************************************************************')
print ('*** INFORMAR QUAL TRIANGULO SE ENCAIXA OS NUMEROS **********')
print ('*****************  RAFAEL MESQUITA *************************')
print ('****** SISTEMAS DE INFORMAÇÃO - UNIS - POO PYTHON **********')
print ('************************************************************')

try: 

   a = float(input("Entre com a medida do lado 1 do triangulo: "))
   b = float(input("Entre com a medida do lado 2 do triangulo: "))
   c = float(input("Entre com a medida do lado 3 do triangulo: "))

except ValueError:

   print("Digite somente numeros para as medidas 1, 2 e 3.")
   sys.exit(1)
   
  #CALCULO VERIFICAR SE O NUMERO E NULO OU NEGATIVO
   
if a<=0 or b<=0 or c<=0 :
   print("Lados nulos ou negativos nao sao aceitos.")
   quit()

   #CALCULO VERIFICAR SE TRIANGULO E INEXISTENTE

if a>=b+c or b>=c+a or c>=a+b :
   print("Triangulo inexistente.")
   quit()

   #CALCULO VERIFICAR SE TRIANGULO E EQUILATERO

if a==b and b==c :
   print("Triangulo equilatero.")

   #CALCULO VERIFICAR SE TRIANGULO E ISOSCELES

elif a==b or b==c or c==a :
   print("Triangulo isosceles.")

   #CALCULO VERIFICAR SE TRIANGULO E ESCALENO

else:
   print("Triangulo escaleno.")
