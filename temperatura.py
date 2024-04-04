#Função de conversão de temperatura
def fahreheint():
    celcius= float(input('Digite a temperatura em celsius: '))
    cfahreheint= ((celcius * 9 /5) + 32)
    return 'A temperatura em fahreheint será: ' + str(cfahreheint)


print(fahreheint())