print('{:=^50}'.format(''))
print('{:^50}'.format('Teste do IMC'))
print('{:=^50}'.format(''))
peso = float(input('Quanto você pesa? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso. Você está muito magro.')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso normal! Parabéns!')
elif imc >= 25  and imc < 30:
    print('Você está em sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade móbita.')
print('{:=^50}'.format(''))