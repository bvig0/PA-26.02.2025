x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
z = int(input('Digite mais um valor:'))
if x > y:
    if y > z:
        print(z)
        print(y)
        print(x)
    else:
        print(y)
        print(z)
        print(x)

else:
    if x > z:
        print(z)
        print(x)
        print(y)
    else:
        print(x)
        print(y)
        print(z)