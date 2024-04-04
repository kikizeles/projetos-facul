def est_civil():
    nome = input('Digite seu nome: ')
    sexo = input('Digite M se for do sexo masculino, e F se for do sexo feminino: ').upper() #.upper serve para deixar tudo em maiusculo
    estado_civil = input('Digite o número que indica seu estado civil: 1. Casado | 2. Solteiro | 3. Viúvo | 4. Divorciado \n Digite: ')
    if sexo == 'F' and estado_civil == '1':
        temp_casado= float(input('Digite o tempo de casado em anos: '))
    print('Muito obrigado pelas informações!')
est_civil()