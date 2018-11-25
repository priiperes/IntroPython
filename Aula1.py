

#Aula 1 

#exercío 1
print('Exercício 1')
print('Se você fizer uma corrida de 10 quilômetros em 43 minutos e 30 segundos, qual será seu tempo médio por milha?')
km=10
milha = km/1.61
tempo=43*60+30
hora= tempo/3600
resultado = hora/milha
print('resultado =',resultado,'h/milha')
print('\n')
print('Qual é a sua velocidade média em milhas por hora?')
velocidade = 1/resultado
print('velocidade =',velocidade,'milha/h')

print('\n')
print('\n')

#exercicio 2
print('Exercício 2')


print('Desde sua varanda você escuta o som do primeiro fogo artificial do reveillon 3 segundos depois de ver a luz, qual a distância?')

#Calcalamos primeiro a distância que os fogos de artificios estão localizados pelo tempo que o som chega
print('\n')
Vsom=343
Vluz=3*10**8
tempo=3
distancia = Vsom*tempo
print('Distancia =', distancia, 'm')

#Agora calculamos o tempo que a luz demora para chegar, baseado na distancia encontrada acima

print('\n')

TempoDaLuz=distancia/Vluz
print('Tempo da Luz =', TempoDaLuz, 's')

print('\n')
print('\n')
#exercicio 3

print('Exercício 3')

print('Ache os zeros da função: y= 3x^2 - 4x -10')

#Para realizar esse calculo, definimos as contantes a, b e c para realizar a formula de baskara

a=3
b=-4
c=-10

#Calculamos Delta

Delta=b*b-(4*a*c)
print('\n')
print('Delta =',Delta)

print('\n')

#calculo das raizes

x1=float((-b + (Delta)**(1/2))/(2*a))
x2=(-b - (Delta)**(1/2))/(2*a)
print('Raiz 1 =',x1)
print('Raiz 2 =',x2)

print('\n')

print('confirmando as raizes encontradas')
print('\n')
y1=a*x1**2+b*x1+c
print('y1= ',y1)

y2=a*x2**2+b*x2+c
print('y2= ',y2)

print('como são proximos de 0, o resultado é compatível')

print('\n')
print('\n')
#exercicio 4
print('Exercício 4')

print('Se, ao meio dia, a sombra de um poste de 5 m de altura tem apenas 50 cm de comprimento no chão, qual o ângulo zenital do sol?')

#O ângulo formado é calculado pelo arcotangente

a=0.5
b=5

AnguloTheta = b/a
print('Angulo Azimute =', AnguloTheta)

print('\n')
print('\n')
#exercicio 5

print('Exercício 5')

print('calcule o seu IMC = M/A^2 (com a massa em Kg e a altura em metros).\n Um valor saudável estara --em geral-- entre 20-25. \n Um bebê de 6 meses gorducho tem 70 cm de comprimento e 11 kg de massa,\n qual o IMC dele?')

#Calculo de Priscyla Peres

M=51
A=1.71
IMC=M/A**A

print('\n')
print('IMC de Priscyla Peres')
print('\n')

print('IMC=', IMC)

print('Como o valor precisa estar entre 20 e 25, o seu IMC está bom e é uma pessoa saudável')

print('\n')

print('IMC do bebê gorducho')
M=11
A=0.7
IMCG=M/A**A

print('IMCG= ', IMCG)



print('\n')
print('\n')

#exercicio 

print('Exercício 6')

print('Calcule a velocidade final de um objeto em queda livre a partir de 3 metros de altura \n (sem resistencia do ar). Calcule o tempo que esse objeto demora para cair. \n')

print('Vamos calcular a velocidade final pela equação de Torrichelli independente do tempo \n')

print('Vf^2=V0^2 + 2gd, onde d é a distância e assumimos que g está no sentindo positivo da direção de propagação da particula e V0^2=0\n')

V=0
g=9.8
d=3
Vf=(V**V + 2*g*d)**(1/2)

print('Vf=', Vf, 'm/s  \n')

print('Usando a formula, Vf=V0+gt \n')

t=Vf/g

print('t=', t, 's')