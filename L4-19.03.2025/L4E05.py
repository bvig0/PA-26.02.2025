# Elabore um algoritmo que leia três números some cinco ao menor valor e mostre o resultado.

x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
z = int(input('Digite mais um valor:'))
if x > y:
    if y > z:
        z = z + 5
        print(z)
    else:
        y = y + 5
        print(y)

else:
    if x > z:
        z = z + 5
        print(z)
    else:
        x = x + 5
        print(x)



    

    

