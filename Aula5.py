# -*- coding: utf-8 -*-


"@author: Priscyla B Peres"


#Exercícios 
print('Exercício 1 ')
    
def max():
    if b>a and b>c:
        maior = b
    if c>a and c>b:
        maior = c
    if a>b and a>c:
        maior = a
    return maior

a = int(input('entre com o primeiro:'))
b = int(input('entre com o segundo:'))
c = int(input('entre com o terceiro:'))

print(max())


print('\n')    

print('Exercício 2')

def soma():
    lista=[2,6,8,7]
    soma = 0
    for i in range(len(lista)):
        soma=soma+lista[i]
    return soma

print(soma())
print('\n')

print('Exercício 3')
def multi():
    lista=[2,6,8,7]
    multi=1
    for i in range(len(lista)):
        multi=multi*lista[i]
    return multi

print(multi())

print('\n')

print('Exercício 4')
def n():
    n = int(input('entre com o numero  = '))
    if n in range (107,673):
       print('{} esta no intervalo'.format(n))
    else:
       print('{} não esta no intervalo '.format(n))

    return n

n()

print('\n')

print('Exercício 5')

def valor():
    lista=[]
    valor = 0
    for i in range(1,5):
        valor = int(input('Entra com o numero:'))
    if valor % 2 == 0:
        lista.append(valor)
    return valor


print(valor())
print('\n')

print('Exercício 6')

n = int(input('digite o numero:'))

w = 1
s = 0

while(w<s):
    if (n%w) == 0:
        s+=w
        w+=1
    else:
        w+=1

if (s==n):
    print('O numero\n'  +  str(n)  +  '\né um numero perfeito')
else:
    print('O número\n'  +  str(n)  +  '\nnăo é perfeito')
    


