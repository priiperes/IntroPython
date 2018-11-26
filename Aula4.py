
#aula 04

def meuverso(palavra):
    print(palavra)
    print(palavra)

def minhacancao (verso1, verso2):
    meuverso(verso1)
    meuverso(verso2)

meuverso(35*90/110)
minhacancao('naaaaa na na nana nanaa','tudum tudum dum')

bicycle= "I want to ride my bicycle"
meuverso(bicycle)

print('---------------------------------------------X------------------------------------------\n')

def gato_duplo (parte1, parte2):
    gato = parte1 + parte2
    meuverso (gato)
linha1 = "blim "
linha2 = "blem! "
gato_duplo(linha1,linha2)

print('---------------------------------------------X------------------------------------------\n')

resultado = meuverso("under pressure")
print(resultado)
print(type(resultado))


print('---------------------------------------------X------------------------------------------\n')

from math import  *
print(sin(pi/3))

print('---------------------------------------------X------------------------------------------\n')


print('Exercícios em sala de aula\n')

print('exercício 1\n')
def do_twice (f):
    f ()
    f ()

def print_spam ():
    print('spam')

do_twice(print_spam)

print('---------------------------------------------X------------------------------------------\n')

#####################################################################################################

def do_twice2 (f,x):
    f(x)
    f(x)
def print_twice(palavras):
    print(palavras)
    print(palavras)
do_twice2(print_twice, 'spam')

print('---------------------------------------------X------------------------------------------\n')

#####################################################################################################

def do_four (f,x):
    do_twice2(f,x)
    do_twice2(f,x)
do_four(print_twice, 'spam')

print('---------------------------------------------X------------------------------------------\n')

print('exercicio 5')

def printpal(coisas):
    print(coisas)

def linha():
    print('+', '-'*10, '+','-'*10,'+')
def coluna():
    linha()
    do_four(printpal,'|            |            | ')
    linha()
    do_four(printpal,'|            |            | ')
    linha()

coluna()


# Exercícios
#exercicio 1
print('Exercício 1')
import time
tempo = time.localtime()
print(time.localtime())
def dia_da_semana(s):
    int (s)
    S = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    return S[s]


def mes(m):
    int (m)
    M = ['janeiro', 'feveiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return M[m-1]

def solu():

    print('\n', 'dia=', tempo.tm_mday,'\n', 'dia da semana=', dia_da_semana(tempo.tm_wday),'\n' , 'mes=', mes(tempo.tm_mon), '\n','ano=', tempo.tm_year, '\n', 'hora=', tempo.tm_hour, ':', tempo.tm_min, ':', tempo.tm_sec)
solu()

print( '\n' )


#exercicio 2
print('Exercício 2')
def fat(n):
    fat=1
    for k in range(n):
        fat=fat*(k+1)
    return fat
print('93!=', fat(93))
print( '\n',)

#exercicio 3
print('Exercício 3')
def iden(x,y):
    if (x>y):
        print('o numero ', x, 'é maior que ', y)
        print('o numero', x, 'é o maior de todos')
    if (x<y):
        print('o numero ', x, 'é menor que ', y)
        print('o numero ', y, 'é o maior')
    if (x==y):
        print('os numeros', x, 'e', y, 'são iguais')

iden(10,20)
iden(6,10)
iden(1224,1224)

print( '\n')

def inde(x,y):
    if (x>y):
        print ('[',y,', ',x, ']')
    if (x<y):
        print ('[',x,', ',y, ']')
    if (x==y):
        print ('[',x,', ',y, ']')

inde(3002,496)
