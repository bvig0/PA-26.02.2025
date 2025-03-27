# Dsenvolva um algoritmo que leia um número e mostre a seguinte mensagem, número maior que dez, se ele for maior que dez e menor igual a dez se ele for menor ou igual a dez.

x = int(input('Digite um valor:'))

if x > 10:
    print('Número maior que dez')
else:
    if x <= 10:
        print('Número menor ou igual a dez')