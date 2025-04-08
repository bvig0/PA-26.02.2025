# Crie um algoritmo que leia dois números, multiplique o menor por 10, e divida o maior por 2, some os seus valores e verifique se o resultado e par, em caso afirmativo exiba a mensagem, o resultado é par, caso contrario, exiba a mensagem, o resultado é impar.

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
if n1 > n2:
    n2 = n2 * 10
    n1 = n1 / 2
    n1 = n2 + n1
else:
    n1 = n1 * 10
    n2 = n2 / 2
    n1 = n2 + n1

if n1 % 2 == 0:
    print('O resultado é par')
else:
    print('O resultado é impar')