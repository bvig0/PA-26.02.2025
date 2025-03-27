# Desenvolva um algoritmo que leia quatro números, some os dois primeiros e subtraia os dois últimos, some os resultados e mostre a seguinte mensagem, resultado maior que dez, caso a afirmação esteja correta ou resultado menor ou igual a dez.

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
n3 = int(input('Digite mais um valor:'))
n4 = int(input('Digite outro valor:'))
n1 = n1 + n2
n2 = n3 + n4
n3 = n2 + n1
if n3 <= 10:
    print('Resultado menor ou igual a dez.')
else: 
    print('Resultado maior que dez.')