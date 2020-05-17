def binario_decimal():
    decimal = 0
    binario = str(input('Digite um número em binario "sair, para terminar": ')).strip().lower()
    cont = len(binario)
    for i in binario:
        if i == '1':
            decimal += 2 ** (cont - 1)
        cont -= 1
    return decimal

def decimal_binario():
    binario = []
    decimal = int(input('Digite um número Decimal: '))
    numero = decimal
    while True:
        if numero == 0 or numero == 1:
            break
        binario.append(numero % 2)
        numero = numero // 2
    if numero == 1:
        binario.append(numero)
    binario.reverse()
    for i in binario:
        print(i, end='')

while True:
    print('\nDigite "sair" para terminar!')
    escolha = str(input('Quer tranformar par Binário ou Decimal [B] ou [D]: ')).lower()
    if escolha == 'sair':
        break
    if escolha == 'b':
        decimal_binario()
    elif escolha == 'd':
        print(binario_decimal())
