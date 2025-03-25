x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
z = int(input('Digite mais um valor:'))
if x > y:
    if x > z:
        print(x)
    else:
        print(z)
else:
    if y > z:
        print(y)
    else:
        print(z)
