#Usei a versão do  Python 3.6.7 para fazer o exercício.

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# F= (C × 9/5) + 32 

#Resposta:
print(' * Resposta exercício 10:')
#Fórmula Matemática para converter Celsius em farenheit = F= (C × 9/5) + 32 .


#Código da solução:
celsius = float(input('Por favor digite a temperatura em graus Celsius: '))
farenheit = ((celsius * 9.0) / 5.0) + 32.0

print('A temperatura em graus Farenheit é = {temperatura} '.format(temperatura = farenheit))
#--------------------------------------------------------------------