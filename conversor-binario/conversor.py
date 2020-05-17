while True:
    decimal = 0
    binario = str(input('Digite um número em binario "sair, para terminar": ')).strip().lower()
    if binario == 'sair':
        break
    cont = len(binario)
    for i in binario:
        if i == '1':
            decimal += 2 ** (cont - 1)
        cont -= 1
    print(decimal)
