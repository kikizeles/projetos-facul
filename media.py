def media():
    nota1= float(input('Insira a primeira nota: '))
    nota2= float(input('insira a segunda nota: '))
    nota3= float(input('Insira a terceira a nota: '))
    media=(nota1+nota2+nota3) / 3
    return media
if media() >= 7 :
    print('Você foi aprovado!')
else:
    print('Voce foi reprovado')
