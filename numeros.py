def ver_num():
    dig= float(input("Digite um numero: "))
    div= dig/2
    return div.is_integer()
if ver_num() == True:
    print('O número é PAR')
else:   print('O número é ímpar')