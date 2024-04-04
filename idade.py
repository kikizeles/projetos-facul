#Conferir a idade pra ver se pode votar
def ver_idade():
    idade= int(input('Escreva sua idade: '))
    if idade <=16:
        print('Você não pode votar!')
    else:
        print('Você pode votar!')
ver_idade()