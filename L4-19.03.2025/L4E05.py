# Elabore um algoritmo que leia três números some cinco ao menor valor e mostre o resultado.

x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
z = int(input('Digite mais um valor:'))
if x > y:
    if y > z:
        x = z + 5
    else:
        x = y + 5

else:
    if x > z:
        x = z + 5
    else:
        x = x + 5

print(x)

    

    

