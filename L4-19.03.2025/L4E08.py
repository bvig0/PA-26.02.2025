# Elabore um algoritmo que leia um número, se ele for maior que dez, some cinco ao seu valor, se ele for menor ou igual, some 20 e mostre se o resultado for maior que vinte e cinco

n = int(input('Digite um valor:'))
if n > 10:
    n = n + 5
    if n > 25:
        print(n)
else:
    n = n + 20
    if n > 25:
        print(n)