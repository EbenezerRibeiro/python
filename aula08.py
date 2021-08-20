n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
e = float(input('Digite a média da sua escola '))
m = (n1 + n2) / 2
if e <= m:
    print('Parabéns, você passou!!!')
else:
    print('Que pena, você não passou ')
print(f'Sua média foi {m}')

