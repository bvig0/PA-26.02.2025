# Elabore um algoritmo que leia dois números, some cinco ao de menor valor, compare os dois valores e mostre o maior

x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
if x > y:
    y = y + 5
else:
    x = x + 5

if x > y:
    print('Este é o maior valor! Sendo ele:', x)
else:
    print('Este é o maior valor! Sendo ele:', y)