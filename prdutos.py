def produto():
    valor = int(100)
    pag = int(input('Escolha uma forma de pagamento: 1. Dinheiro | 2. Cartão de crédito | 3. Divido em 2x | 4. Dividido em 3x c/ juros: '))
    if pag == 1:
        pag1 = (10/100)*valor
        pag2 = (valor - pag1)
        print('O valor será:' , pag2)
    elif pag == 2:
        pag3 = (15/100)*valor
        pag4 = (valor - pag3)
        print('O valor será:' , pag4)
    elif pag == 3:
        pag5 = (valor / 2)
        print('O valor será:' , pag5)
    elif pag == 4:
        pag6 = (10/100)*valor
        pag7 = (valor + pag6)
        pag8 = (pag7 / 3)
        print('O valor será:' ,pag8)
produto()