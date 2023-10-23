# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR

reta1 = int(input("digite a primera reta: "))
reta2 = int(input("digite a segunda reta: "))
reta3 =int(input("digite a terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É um triangulo')
else:
    print('Não é um triangulo')