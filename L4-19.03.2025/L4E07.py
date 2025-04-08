#  Crie um algoritmo que leia três números e mostre seus valores em ordem crescente.

x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
z = int(input('Digite mais um valor:'))
if x < y:
    if x < z:
        print(x)
        if y < z:
            print(y)
            print(z)
        else:
            print(z)
            print(y)
    else:
        print(z)
        print(x)
        print(y)

else:
    if y < z:
        print(y)
        if x < z:
            print(x)
            print(z)
        else:
            print(z)
            print(x)
    else:
        print(z)
        print(y)
        print(x)