velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade >80:
    print('\033[1;31;43mMultado! Voce excedeu o limite permitido que é de 80Km/h\033[m')
    multa = (velocidade-80) * 7
    print(' Você deve pagar uma multa de R${:.2F}!'. format(multa))
print('Tenha um bom dia! Digija com segurança!')