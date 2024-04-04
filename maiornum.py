def maior_3():
    num1= float(input("Digite o primeiro número: "))
    num2= float(input("Digite o segundo número: "))
    num3= float(input("Digite o terceiro número: "))
    numtodos= (num1, num2, num3)
    return max(numtodos)
print('O maior número será: ', maior_3())