#Usei a versão do  Python 3.6.7 para fazer o exercício.

#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).

#Resposta:
print(' * Resposta exercício 9:')
#Fórmula Matemática para converter farenheit em Celsius =  C = (5 * (F-32) / 9).

#Código da solução:
farenheit = float(input('Por favor digite a temperatura em Graus Farenheit: '))
celsius = 5 * (farenheit - 32) / 9.0
print ('A Temperatura em Graus Celsius é = {temperatura} '.format(temperatura = celsius))
#---------------------------------------------------------------------