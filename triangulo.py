def iden_tri():
    l1=float(input('Digite o primeiro lado do triângulo: '))
    l2=float(input('Digite o segundo lado do triângulo: '))
    l3=float(input('Digite o terceiro lado do triângulo: '))
    if l1 == l2 == l3:
        print('Triangulo equilátero')
    elif l1 == l2 or l3 == l2 or l3 ==l1:
        print('Triangulo isósceles')
    else:
        print('Triangulo escaleno')
iden_tri()
