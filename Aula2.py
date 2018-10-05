# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:26:06 2018

@author: Priscyla B Peres
"""
import math
 #aula 2

#exercício 1
largura =17
altura=12.0
delimitador="."

print(largura/2)
print(largura/2.0)
print(altura/3)
print(1+2*5)
print(delimitador*5)

#exercício 2
r=5
pi=3.1415
volume=(4/3)*math.pi*r**3

#exercício 3
p=24.95 #preço do livro
des=0.4 #desconto do livro
env=3.0 #preco do primeiro envio
adc=0.75 #exemplar adicional
n=60 #número de livros comprados
custo = (p-p*des)*60 + env +adc*(n-1)
print(custo,'reais')

#exercício 4
co=632.8*10**(-9)  #comprimento de onda
D=1.98 #distância do anteparo a fenda
d=0.25*10**(-9) #espaçamento entre as fendas
delta_y=((co)*D )/d
print(delta_y,'m')
