#Usei a versão do  Python 3.6.7 para fazer o exercício.

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#Resposta:
print(' * Resposta exercício 6:')
#formula Matemática para cálculo da Área do raio =  A = π . r2 | Área é igual a pi vezes raio ao quadrado.
# Para pegar o Pi optei por usar a bibilioteca math por isso primeiro é necessário importar a biblioteca.

#Código da solução:
import math
raio = float(input("Informe a medida do raio de um circulo: "))
print ("A área do circulo de raio", raio, "é = ", (math.pi*(raio**2)))
#-------------------------------------------------------------
