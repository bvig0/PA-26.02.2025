x = int(input('Digite um valor:'))
y = int(input('Digite outro valor:'))
if x > y:
    y = y + 5
    if x < y:
        print('Este é o maior valor! Sendo ele:', y)
    else:
        print('Este é o maior valor! Sendo ele:', x)

else:
    x = x + 5
    if x < y:
        print('Este é o maior valor! Sendo ele:', y)
    else:
        print('Este é o maior valor! Sendo ele:', x)
