n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
r = n1 + n2
if r<20:
    n1 = n1 * 10
    n2 = n2 * 10
    print('O valor é valido, sendo ele', n1)
    print('O valor é valido, sendo ele', n2)