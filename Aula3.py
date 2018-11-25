# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:07:40 2018

@author: Priscyla B Peres
"""

#aula 3 
import math


cateto_oposto = 4
cateto_adjacente = 2
tangente_theta = cateto_oposto/cateto_adjacente
theta = math.atan(tangente_theta)
print(theta, 'em radianos')
math.degrees(theta)

theta_graus = theta*180/math.pi
print(theta_graus,'°')

theta_graus_alter = math.degrees(math.acos(math.sqrt(2)/2))
print(theta_graus_alter,'°')

x = math.sin(theta_graus/360.0 * 2 * math.pi)
print(x)

x1 = math.exp(math.log (x + 1))
print(x1)

horas = 2
minutos = horas * 60

print(minutos)

def print_poema():
     print('batatinha quando nasce se esparrama pelo chão, ')
     print('meu voto no Ciro vai ')
     print('faze-lo campeão')
    
print(print_poema)
type(print_poema)


print_poema()

print('exercicio 1: Crie uma funcão que tome um argumento e imprima o valor e o tipo dele.  \n')

def tipo(x):
    print(type(x))

tipo(2.2)
tipo('pudim')
tipo(1993)

print('------------------------------------------------------X----------------------------------------------------------------------\n')

print('exercicío 2: Crie uma função que calcule e imprima velocidade media de um objeto a partir de uma posição inicial\n'
      'e final e o tempo transcorrido para um objeto em MRU. Também crie uma funcão que calcule e imprima a velocidade de um\n'
      'objeto a partir da aceleração constante e o tempo (MRUA) (p.ex. queda libre).\n')

def velocidade_media(x0, x, t):
    Vm=(x-x0)/t
    print('Vm =', Vm, 'anos luz/séculos')

velocidade_media(2,10,5)

def velocidade_media_2(v0, a, t2):
    Vf=v0+a*t2
    print('Vm =', Vf, 'anos luz/séculos')

velocidade_media_2(0,2,3)

print('--------------------------------------X-----------------------------------------------------\n')
print('exercicío 3: Crie uma funcão para calcular o ângulo zenital do sol (da semana passada) \n'
      'tomando como argumento as medidas da altura e o comprimento da sombra.\n')

import math
cateto_oposto = 0.5
cateto_adjacente = 5
tg_theta = cateto_oposto/cateto_adjacente
theta = math.atan(tg_theta)
print(theta, 'em radianos')
theta2=math.degrees(theta)
print(theta2, 'graus')

print('--------------------------------------X-----------------------------------------------------\n')

print('exercício 4: Crie uma função que faça a conversão de uma medida inicialmente em milhas para m, e outra para o inverso;\n'
      'uma de horas para segundos, e o inverso. Utilize estas funções para resolver novamente o primeiro exercício da semana passada (da corrida).\n'
      'Se uma pessoa demora 30 minutos em 4 milhas, qual velocidade media em km/h ? e o tempo medio por kilometro? \n')

def conversor(m):
    mi=1609.34*m
    print(mi, 'milhas')
conversor(3)

def conversor2(mi):
    m=mi/1609.34
    print(m, 'metros')

conversor2(8546)

def hora(s):
    h=s/3600
    print(h, 'horas')

hora(9854)

def segundos(h):
    s=3600*h
    print(s, 'segundos')

segundos(6.87)

print('--------------------------------------X-----------------------------------------------------\n')

print('exercício 5: Crie funções para calcular os outros exemplos das aulas anteriores: \n'
      ' IMC, volume de uma esfera, distancia entre pontos de máximos de difração.\n'
      'Decida quais serão os argumentos e o valor retornado. \n ')
def IMC(massa,altura):
	IMC = massa/altura**2
	return IMC
#Escrevendo um exemplo
print('IMC = ',IMC(11,0.7),'kg/m²')

def volume_esfera(raio):
	volume = (4/3)*math.pi*raio**3
	return volume

#Escrevendo um exemplo
print('IMC = ',IMC(11,0.7),'kg/m²')
import math
def volume_esfera(raio):
	volume = (4/3)*math.pi*raio**3
	return volume
#Escrevendo um exemplo
print('volume da esfera = ',volume_esfera(5))

def difracao(D,d,comp_onda):
	#Levando em conta que as unidades inseridas estão corretas, iguais e em metro
	delta_y=comp_onda*D/d
	return delta_y
#Escrevendo um exemplo
print('delta_y da difração = ', difracao(1.98,0.25*10**(-3),632.8*10**(-9)), 'm')

print('--------------------------------------X-----------------------------------------------------')












