#Conferir o imc da pessoa

peso= float(input('Digite seu peso: '))
altura= float(input('Digite sua altura: '))
imc= peso / (altura**2)
print(imc)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc <24.9:
    print('Esse é seu peso ideal!')
elif imc <29.9:
    print('Você está sobrepeso!')
else:
    print('Você está obeso!')
